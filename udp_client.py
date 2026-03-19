import socket
import time
from data_generator import generate_data

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = generate_data()

    # Convert dict → CSV string
    message = f"{data['junction_id']},{data['timestamp']},{data['vehicle_count']},{data['queue_length']},{data['waiting_time']},{data['signal_state']}"

    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    print("Sent:", message)

    time.sleep(2)