# 🚦 CN Jackfruit – Smart Traffic Monitoring System

> A network-based traffic monitoring pipeline that simulates real-world urban traffic, extracts live data via TraCI, and streams it over UDP to a central server for analysis and visualization.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Folder Structure](#folder-structure)
- [Setup & Installation](#setup--installation)
- [Running the Project](#running-the-project)
- [Traffic Scenarios](#traffic-scenarios)
- [Traffic Metrics](#traffic-metrics)
- [Signal State Reference](#signal-state-reference)
- [Sample Output](#sample-output)

---

## Overview

The **Smart Traffic Monitoring System** is a computer networks project that simulates real-world traffic conditions, extracts real-time data, and transmits it across a network to a central server for processing.

The system is built around three core stages:

| Stage | Component | Role |
|-------|-----------|------|
| 1 | SUMO + TraCI | Simulate traffic & extract live metrics |
| 2 | UDP Socket Layer | Transmit data over the network |
| 3 | Server + Client | Receive, process, and display traffic data |

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    SUMO Simulation                       │
│   (Scenario1_low / Scenario2_med / Scenario3_high)      │
└────────────────────────┬────────────────────────────────┘
                         │ TraCI (live data extraction)
                         ▼
              ┌──────────────────────┐
              │  extract_traffic_    │
              │     data.py          │
              │  data_generator.py   │
              └──────────┬───────────┘
                         │ JSON over UDP
                         ▼
              ┌──────────────────────┐
              │      server.py       │  ◄── UDP Server
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │    udp_client.py     │  ◄── Client Display
              └──────────────────────┘
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| [SUMO](https://sumo.dlr.de/) | Urban traffic simulation engine |
| [TraCI](https://sumo.dlr.de/docs/TraCI.html) | Python API to interface with live SUMO simulation |
| Python 3.x | Core scripting language |
| UDP Sockets | Fast, lightweight network transport layer |
| JSON | Data serialization format for traffic metrics |

### What is TraCI?
TraCI (**Tra**ffic **C**ontrol **I**nterface) allows a Python script to communicate with a running SUMO simulation in real time. It is used here to extract live metrics such as vehicle count, queue lengths, waiting times, and signal states from each intersection.

---

## Prerequisites

Make sure you have the following installed before running the project:

- **Python** 3.8 or higher
  ```bash
  python --version
  ```

- **SUMO** (Simulation of Urban Mobility) — [Installation Guide](https://sumo.dlr.de/docs/Installing/index.html)
  ```bash
  sumo --version
  ```

- **TraCI** Python library (bundled with SUMO, or install via pip)
  ```bash
  pip install traci
  ```

- Ensure the `SUMO_HOME` environment variable is set:
  ```bash
  # Linux / macOS
  export SUMO_HOME=/path/to/sumo

  # Windows
  set SUMO_HOME=C:\path\to\sumo
  ```

---

## Folder Structure

```
CN_jackfruit/
│
├── SUMO_Simulation/
│   └── Scenarios/
│       ├── Scenario1_low/        # Low traffic density configuration
│       ├── Scenario2_med/        # Medium traffic density configuration
│       └── Scenario3_high/       # High traffic density configuration
│
├── data_generator.py             # Generates/simulates traffic data
├── server.py                     # UDP server — receives and processes data
├── udp_client.py                 # UDP client — connects to server and displays data
├── udp_server_test.py            # Unit/integration tests for the UDP server
│
├── scenario1_output.json         # Captured output from Scenario 1 (low)
├── scenario2_output.json         # Captured output from Scenario 2 (medium)
├── scenario3_output.json         # Captured output from Scenario 3 (high)
│
└── README.md                     # Current file being viewed, contains overview about project
```

---

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/bhuvidange/CN_jackfruit.git
cd CN_jackfruit
```

**2. Install Python dependencies**
```bash
pip install traci
```

**3. Verify SUMO is accessible**
```bash
sumo-gui --version
```

---

## Running the Project

> **Important:** Components must be started in this exact order.

### Step 1 — Start the UDP Server
```bash
python server.py
```
The server will begin listening for incoming UDP packets on the configured port.

### Step 2 — Start the SUMO Simulation + Data Extraction
```bash
cd SUMO_Simulation/Scenarios
python extract_traffic_data.py
```
This launches the SUMO simulation and uses TraCI to extract live traffic metrics, which are serialized to JSON and sent over UDP.

### Step 3 — Start the UDP Client
```bash
python udp_client.py
```
The client connects to the server and displays the incoming traffic data stream in real time.

---

## Traffic Scenarios

Three pre-configured traffic scenarios are included to test the system under different load conditions:

| Scenario | Folder | Description |
|----------|--------|-------------|
| Scenario 1 | `Scenario1_low/` | Low traffic density — light vehicle volume |
| Scenario 2 | `Scenario2_med/` | Medium traffic density — moderate congestion |
| Scenario 3 | `Scenario3_high/` | High traffic density — peak congestion conditions |

Each scenario folder contains the required SUMO network and route configuration files. Switch between scenarios by pointing `extract_traffic_data.py` to the appropriate folder.

---

## Traffic Metrics

The following metrics are extracted per simulation step and transmitted as a JSON payload:

| Metric | Description |
|--------|-------------|
| `vehicle_count` | Total number of vehicles currently in the simulation |
| `queue_north` | Queue length of vehicles waiting at the North lane |
| `queue_south` | Queue length of vehicles waiting at the South lane |
| `queue_east` | Queue length of vehicles waiting at the East lane |
| `queue_west` | Queue length of vehicles waiting at the West lane |
| `total_waiting_time` | Cumulative waiting time across all vehicles (seconds) |
| `signal_state` | Current traffic light phase |
| `timestamp` | Simulation step timestamp |

---

## Signal State Reference

| Signal State | Meaning |
|---|---|
| `NS_GREEN` | North–South lanes have right of way |
| `EW_GREEN` | East–West lanes have right of way |
| `YELLOW` | Transition phase between signal changes |
| `ALL_RED` | All directions stopped (clearance phase) |

---

## Sample Output

Below is an example JSON payload transmitted from the simulation to the server:

```json
{
  "timestamp": 42.0,
  "vehicle_count": 18,
  "queue_north": 3,
  "queue_south": 5,
  "queue_east": 2,
  "queue_west": 4,
  "total_waiting_time": 134.5,
  "signal_state": "NS_GREEN"
}
```

Pre-captured outputs for all three scenarios are available in:
- `scenario1_output.json`
- `scenario2_output.json`
- `scenario3_output.json`

---

