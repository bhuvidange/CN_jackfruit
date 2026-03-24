
import socket
import json
import threading
import tkinter as tk

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

root = tk.Tk()
root.title("Smart Traffic Monitoring System")
root.geometry("400x300")

title = tk.Label(root, text="Traffic Monitoring Dashboard", font=("Arial",16))
title.pack(pady=10)

vehicle_label = tk.Label(root, text="Vehicles: 0", font=("Arial",12))
vehicle_label.pack()

queue_label = tk.Label(root, text="Queue Length: 0", font=("Arial",12))
queue_label.pack()

wait_label = tk.Label(root, text="Waiting Time: 0", font=("Arial",12))
wait_label.pack()

status_label = tk.Label(root, text="Status: NORMAL", font=("Arial",14))
status_label.pack(pady=10)

def analyze(queue, wait):

    if queue < 5 and wait < 10:
        return "NORMAL"

    elif queue < 15:
        return "MODERATE"

    else:
        return "SEVERE"

def listen():

    while True:

        data, addr = sock.recvfrom(65535)
        packet = json.loads(data.decode())

        north = packet["north_queue"]
        south = packet["south_queue"]
        east = packet["east_queue"]
        west = packet["west_queue"]

        total_queue = north + south + east + west
        waiting_time = packet["waiting_time"]

        status = analyze(total_queue, waiting_time)

        vehicle_label.config(text=f"Vehicles: {packet['vehicle_count']}")
        queue_label.config(text=f"Queue Length: {total_queue}")
        wait_label.config(text=f"Waiting Time: {waiting_time}")

        if status == "NORMAL":
            status_label.config(text="🟢 NORMAL", fg="green")

        elif status == "MODERATE":
            status_label.config(text="🟡 MODERATE", fg="orange")

        else:
            status_label.config(text="🔴 SEVERE", fg="red")

thread = threading.Thread(target=listen, daemon=True)
thread.start()
root.mainloop()
