# This program acts as a UDP client that sends simulated traffic data to a server.
# It reads pre-generated traffic records from a JSON file, processes each record
# using a helper function, converts the data into a comma-separated string format,
# and sends it over the network at regular intervals (1 second). This simulates
# real-time traffic data streaming from a traffic system to a monitoring server.

import socket   # Used for network communication
import time     # Used to create delays between sending packets
import json     # Used to read data from JSON file
from data_generator import generate_data    # Function to process each record

# Server configuration (IP address and port number)
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
SEND_INTERVAL = 0.1  # Time gap between sending each message (in seconds)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open and load traffic data from JSON file
with open("Tjunc.json", "r") as f:
    records = json.load(f)

packet_id = 0  # To keep packet count for tracking and loss detection

# Loop through each record in the JSON file, process it, and send to the server
for record in records:
     # Generate structured data from raw record
    data = generate_data(record)

    # Convert data into a comma-separated string message
    message = (
        f"{packet_id},"
        f"{data['timestamp']},"          # Current timestamp
        f"{data['simulation_time']},"    # Simulation time
        f"{data['vehicle_count']},"      # Total number of vehicles
        f"{data['north_queue']},"        # Vehicles waiting in north direction
        f"{data['south_queue']},"        # Vehicles waiting in south direction
        f"{data['east_queue']},"         # Vehicles waiting in east direction
        f"{data['west_queue']},"         # Vehicles waiting in west direction
        f"{data['waiting_time']},"       # Total waiting time
        f"{data['signal_state']}")        # Current traffic signal state

    print("Sent:", message) # Print the message being sent for debugging purposes

    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    packet_id += 1  # Increment packet ID for the next message

    # Wait for specified interval before sending next data
    time.sleep(SEND_INTERVAL)

# Close the socket after sending all data
client_socket.close()