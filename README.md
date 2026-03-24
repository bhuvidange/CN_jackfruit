# CN jackfruit
CN jackfruit-Smart Traffic Monitoring System

Project Overview:
The Smart Traffic Monitoring System is a network-based traffic monitoring solution that simulates real-world traffic conditions, extracts real-time data, and transmits it to a central system for analysis.

This project integrates:

- Traffic Simulation (SUMO)
- Real-time Data Extraction (TraCI + Python)
- Network Communication (UDP)
- Data Processing & Analysis

The system is designed to monitor congestion over a course of time, thus helping enable intelligent traffic control strategies.

Technologies Used
* SUMO (Simulation of Urban Mobility) – Traffic simulation
* TraCI (Traffic Control Interface) – Real-time interaction with SUMO
* Python – Data extraction and networking
* UDP Sockets – Fast data transmission
* JSON – Data storage format

Prerequisites:
In order to run this project, it is essential to have SUMO and the required python dependency (TraCI) installed

Running the project:
1) Navigate to Scenario folder and run the simulation with data extraction
    `cd SUMO_Simulation/Scenarios`
    Now say we want to run Scenario1, we would do so as follows:
    `python extract_traffic_data.py Scenario1_low/scenario.sumocfg scenario1_output.json`

    The above code will do the following:
    - Launch SUMO GUI
    - Run simulation
    - Extract real-time traffic data
    - Save it into scenario1_output.json
    

Traffic metrics extracted:
* Total vehicle count
* Queue length per direction (North, South, East, West)
* Total waiting time
* Traffic signal state
* Simulation timestamp

Signal State Interpretation:
NS_GREEN → North-South flow active
EW_GREEN → East-West flow active
YELLOW → Transition phase
ALL_RED → All signals stopped


Making use of Socket Programming and concepts of UDP packet transmission to create a fast congestion monitoring
system that informs us of the changing congestion rates throughout the lifespan of the simulation 