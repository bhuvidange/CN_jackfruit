SIGNAL_STATE_MAP = {
    "NS_GREEN": "GREEN",
    "EW_GREEN": "GREEN",
    "ALL_RED":  "RED",
    "YELLOW":   "YELLOW",
}

def generate_data(sumo_record):
    return {
        "timestamp":       sumo_record["timestamp"],
        "simulation_time": sumo_record["simulation_time"],
        "vehicle_count":   sumo_record["vehicle_count"],
        "north_queue":     sumo_record["north_queue"],
        "south_queue":     sumo_record["south_queue"],
        "east_queue":      sumo_record["east_queue"],
        "west_queue":      sumo_record["west_queue"],
        "waiting_time":    sumo_record["waiting_time"],
        "signal_state":    SIGNAL_STATE_MAP.get(sumo_record["signal_state"], "RED"),
    }
