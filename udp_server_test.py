import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 9999))

print("Server listening...")

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()

    # Split CSV
    fields = message.split(",")

    print("Received:")
    print(" Junction:", fields[0])
    print(" Timestamp:", fields[1])
    print(" Vehicle Count:", fields[2])
    print(" Queue Length:", fields[3])
    print(" Waiting Time:", fields[4])
    print(" Signal:", fields[5])
    print("------------------------")