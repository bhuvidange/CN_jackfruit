# CN jackfruit




The Smart Traffic Monitoring System is a network-based solution that simulates real-world traffic conditions, extracts real-time data, and transmits it to a central system for analysis.

This project combines multiple components to create a complete traffic monitoring pipeline:

Traffic Simulation (SUMO) – simulates vehicle movement
Real-time Data Extraction (TraCI + Python) – collects live traffic data
Network Communication (UDP) – sends data across the network
Data Processing & Analysis – formats and interprets traffic data

The system monitors congestion over time and helps in understanding traffic patterns and improving traffic control strategies.

Technologies Used
SUMO (Simulation of Urban Mobility) – traffic simulation
TraCI (Traffic Control Interface) – interaction with the simulation
Python – data extraction and networking
UDP Sockets – data transmission
JSON – data storage
What is TraCI?

TraCI (Traffic Control Interface) is a tool that allows a Python program to communicate with the SUMO simulation while it is running.

It is used to:

Read live data such as vehicle count, queue lengths, and signal states
Access simulation data at each time step


Running the Project
Open a terminal in the project directory.
Run the simulation and start data extraction using the provided Python script.
The script will:
Launch the SUMO simulation
Extract real-time traffic data using TraCI
Save data to a JSON file and/or transmit it via UDP
    

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
