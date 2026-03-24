import socket
import time
import json
from data_generator import generate_data

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
SEND_INTERVAL = 1.0

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open("scenario1_output.json", "r") as f:
    records = json.load(f)

for record in records:
    data = generate_data(record)
    message = (
        f"{data['timestamp']},"
        f"{data['simulation_time']},"
        f"{data['vehicle_count']},"
        f"{data['north_queue']},"
        f"{data['south_queue']},"
        f"{data['east_queue']},"
        f"{data['west_queue']},"
        f"{data['waiting_time']},"
        f"{data['signal_state']}"
    )
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    print("Sent:", message)
    time.sleep(SEND_INTERVAL)

client_socket.close()
