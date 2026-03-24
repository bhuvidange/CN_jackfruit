# **CN Jackfruit – Smart Traffic Monitoring System**

The Smart Traffic Monitoring System is a network-based solution that simulates real-world traffic conditions, extracts real-time data, and transmits it to a central system for analysis.

This project combines multiple components to create a complete traffic monitoring pipeline:

* **Traffic Simulation (SUMO)** – simulates vehicle movement  
* **Real-time Data Extraction (TraCI + Python)** – collects live traffic data  
* **Network Communication (UDP)** – sends data across the network  
* **Data Processing & Analysis** – formats and interprets traffic data  

## **Technologies Used**

* SUMO (Simulation of Urban Mobility)  
* TraCI (Traffic Control Interface)  
* Python  
* UDP Sockets  
* JSON  

## **What is TraCI?**

TraCI allows a Python program to communicate with a SUMO simulation while it is running.  
It is used to read live data such as vehicle count, queue lengths, and signal states.

## **Running the Project**

1. **Run the SUMO Simulation** – Start the traffic simulation using the Python script.  
2. **Run the Server** – Start the server script to receive traffic data via UDP.  
3. **Run the Client** – Start the client script to receive and display data from the server.  

> **Important:** Run the components in this order: **Simulation → Server → Client**.

## **Traffic Metrics Extracted**

* Total vehicle count  
* Queue length per direction (North, South, East, West)  
* Total waiting time  
* Traffic signal state  
* Simulation timestamp  

## **Signal State Interpretation**

* **NS_GREEN** → North-South flow active  
* **EW_GREEN** → East-West flow active  
* **YELLOW** → Transition phase  
* **ALL_RED** → All signals stopped  

The system uses UDP socket programming to create a fast congestion monitoring system that tracks changing congestion rates throughout the simulation.
