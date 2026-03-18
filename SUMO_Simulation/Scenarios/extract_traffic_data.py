import traci
import sys
import json
from datetime import datetime

config_file = sys.argv[1]
output_json = sys.argv[2]

sumoBinary = "sumo-gui"

sumoCmd = [sumoBinary, "-c", config_file]

traci.start(sumoCmd)
data_log = []

def interpret_signal(state):
    if "G" in state and state.startswith("G"):
        return "NS_GREEN"
    elif "G" in state and len(state) > 1 and state[1] == "G":
        return "EW_GREEN"
    elif "y" in state or "Y" in state:
        return "YELLOW"
    return "ALL_RED"

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    vehicles = traci.vehicle.getIDList()
    vehicle_count = len(vehicles)
    north_q = 0
    south_q = 0
    east_q = 0
    west_q = 0
    waiting_time = 0
    for v in vehicles:
        waiting_time += traci.vehicle.getWaitingTime(v)
        if traci.vehicle.getSpeed(v) < 0.1:
            lane = traci.vehicle.getLaneID(v)
            if "north_in" in lane:
                north_q += 1
            elif "south_in" in lane:
                south_q += 1
            elif "east_in" in lane:
                east_q += 1
            elif "west_in" in lane:
                west_q += 1
    tls_id = traci.trafficlight.getIDList()[0]
    raw_state = traci.trafficlight.getRedYellowGreenState(tls_id)
    signal_state = interpret_signal(raw_state)
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
    data_log.append(step_data)
traci.close()
with open(output_json, "w") as f:
    json.dump(data_log, f, indent=4)