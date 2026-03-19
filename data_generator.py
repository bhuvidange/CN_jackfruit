import time
import random

def generate_data():
    return {
        "junction_id": random.choice([
            "SilkBoard",
            "KR_Puram",
            "BTM_Layout",
            "Marathahalli",
            "Whitefield"
        ]),
        "timestamp": int(time.time()),
        "vehicle_count": random.randint(0, 30),
        "queue_length": random.randint(0, 15),
        "waiting_time": random.randint(0, 60),
        "signal_state": random.choice(["RED", "GREEN", "YELLOW"])
    }