import socket      # Used for network communication
import time        # Used to add delay between sending messages
import json        # Used to read data from JSON file
from data_generator import generate_data   # Function to process each record

# Server configuration (IP address and port number)
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

# Time gap between sending each message (in seconds)
SEND_INTERVAL = 1.0

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open and load traffic data from JSON file
with open("scenario1_output.json", "r") as f:
    records = json.load(f)

sequential_id = 0  # Initialize sequential ID for messages

# Loop through each record in the JSON file
for record in records:
    
    # Generate structured data from raw record
    data = generate_data(record)
    
    # Convert data into a comma-separated string message
    message = (
        f"{sequential_id},"             # Sequential ID for tracking
        f"{data['timestamp']},"          # Current timestamp
        f"{data['simulation_time']},"    # Simulation time
        f"{data['vehicle_count']},"      # Total number of vehicles
        f"{data['north_queue']},"        # Vehicles waiting in north direction
        f"{data['south_queue']},"        # Vehicles waiting in south direction
        f"{data['east_queue']},"         # Vehicles waiting in east direction
        f"{data['west_queue']},"         # Vehicles waiting in west direction
        f"{data['waiting_time']},"       # Total waiting time
        f"{data['signal_state']}"        # Current traffic signal state
    )
    
    # Send the message to the server
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    
    # Print the sent message (for debugging/monitoring)
    print("Sent:", message)
    
    sequential_id += 1  # Increment sequential ID for next message
    
    # Wait for specified interval before sending next data
    time.sleep(SEND_INTERVAL)

# Close the socket after sending all data
client_socket.close()