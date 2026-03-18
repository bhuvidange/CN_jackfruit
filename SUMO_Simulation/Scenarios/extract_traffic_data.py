import traci
import sys
import json
from datetime import datetime

config_file = sys.argv[1]   #Reads SUMO configuration file path from command line argument
output_json = sys.argv[2]   #Reads 2nd command line argument (where simulation data will be saved in JSON format)

sumoBinary = "sumo-gui"     #Use "sumo" for command-line version, "sumo-gui" for graphical interface

sumoCmd = [sumoBinary, "-c", config_file]   #Constructs the command to start SUMO with the specified configuration file

traci.start(sumoCmd)    #Starts the SUMO simulation using the TraCI interface
data_log = []

# Function to interpret the traffic light state based on the raw state string from SUMO into readable text
def interpret_signal(state):
    if "G" in state and state.startswith("G"):
        return "NS_GREEN"   # NS_GREEN indicates that the north-south direction has a green light
    elif "G" in state and len(state) > 1 and state[1] == "G":
        return "EW_GREEN"
    elif "y" in state or "Y" in state:
        return "YELLOW"
    return "ALL_RED"

# Main simulation loop: runs until there are no more expected vehicles in the simulation

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()  #Advances the simulation by one step 
    vehicles = traci.vehicle.getIDList()    #Gets a list of all vehicle IDs currently in the simulation
    vehicle_count = len(vehicles)   #Counts the number of vehicles currently in the simulation
    
    #Initializes queue counters for each direction to zero
    north_q = 0
    south_q = 0
    east_q = 0
    west_q = 0
    waiting_time = 0

    for v in vehicles:
        waiting_time += traci.vehicle.getWaitingTime(v)
        if traci.vehicle.getSpeed(v) < 0.1:  #If the vehicle is essentially stopped, we consider it part of the queue
            lane = traci.vehicle.getLaneID(v)
            if "north_in" in lane:  #If the lane ID contains north incoming, we increment the north queue counter
                north_q += 1
            elif "south_in" in lane:
                south_q += 1
            elif "east_in" in lane:
                east_q += 1
            elif "west_in" in lane:
                west_q += 1
    tls_id = traci.trafficlight.getIDList()[0]  #Gets the ID of the first traffic light in the simulation (assuming there's only one)

    '''
    SUMO simulation we have made is using a single junction system with one traffic light controlling the flow of vehicles from four directions (north, south, east, west).
    The traffic light operates in a fixed cycle, alternating between allowing north-south traffic to go while stopping east-west traffic, and then allowing east-west traffic to go while stopping north-south traffic.
    The traffic light also has a yellow phase in between the green phases for safety.
    The data we are collecting includes the number of vehicles currently in the simulation,
    the queue lengths for each direction, the total waiting time of all vehicles, and the current state of the traffic light (which direction has the green light or if it's yellow or all red).
    Project has been designed such that it can be easily extended to more complex scenarios with multiple junctions and traffic lights by modifying the data collection logic to handle multiple traffic light IDs and their respective states.

    '''

    raw_state = traci.trafficlight.getRedYellowGreenState(tls_id)   #Raw state of the traffic light
    signal_state = interpret_signal(raw_state)  #Converts the raw state into a more human-readable format (e.g., NS_GREEN, EW_GREEN, YELLOW, ALL_RED)
    step_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "simulation_time": traci.simulation.getTime(),
        "vehicle_count": vehicle_count,
        "north_queue": north_q,
        "south_queue": south_q,
        "east_queue": east_q,
        "west_queue": west_q,
        "waiting_time": waiting_time,
        "signal_state": signal_state
    }
    data_log.append(step_data)  #Appends the collected data for the current simulation step to the data log created earlier
traci.close()
with open(output_json, "w") as f:   #Outputs the collected data log to a JSON file specified by the second command line argument
    json.dump(data_log, f, indent=4)