# Dobot Arm Automation with Python

## Overview
This project involves controlling two Dobot robotic arms using the **Dobot API**. The system automates pick-and-place operations using pre-defined coordinates stored in CSV files. The project includes server-client communication, pose retrieval, and the use of suction cups for item handling.

### Components:
- **Dobot API**: Used to control the robotic arm and effectors like the suction cup.
- **CSV Files (`coordinates_for_arm_1.csv` and `coordinates_for_arm_2.csv`)**: Contain the coordinates for different pick-and-place positions for both arms.
- **Server-Client Communication**: A server waits for input from a client (e.g., pressing keys or commands), and the arms perform actions like moving to different positions based on the received commands.

## Files Overview

### 1. `arm1.py`
This file controls the first Dobot arm by reading coordinates from the `coordinates_for_arm_1.csv` file. The robot performs a sequence of movements to pick up an object, move it, and place it in a new location. It uses the suction cup effector to pick up the object and then place it in a different position.

### 2. `arm2.py`
This file handles the second Dobot arm and is used to automate the second part of the pick-and-place operation. The arm's movements are determined based on the coordinates stored in the `coordinates_for_arm_2.csv`. The arm listens for input through a keyboard interface and then sends commands to a server, which processes the actions.

### 3. `coord_init.py`
This script allows for the manual recording of coordinates for the robotic arm. It prompts the user to position the arm at different locations (home, pick up, pick down, place up, place down) and saves the coordinates into a CSV file. This is useful for setting up initial positions before starting automation.

### 4. `pose.py`
This script continuously prints the current pose of the robotic arm, including its `x`, `y`, and `z` coordinates. It helps in monitoring the real-time position of the arm for debugging and calibration.

### 5. `server.py`
This file implements a basic server that listens for incoming client requests over TCP. It receives an index value from the client and sends back a response (either an acknowledgment or an action code). This is used to control the pick-and-place operation based on input from the client.

## Requirements

- Python 3.x
- Dobot API library (installed through `pip install dobot-api`)
- `keyboard` library for keyboard interaction (install via `pip install keyboard`)
- `socket` library for server-client communication
- CSV files with predefined coordinates for each arm (e.g., `coordinates_for_arm_1.csv`, `coordinates_for_arm_2.csv`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dobot-arm-automation.git
   cd dobot-arm-automation
   ```
2. Install the required dependencies:

  ```bash
  Copy code
  pip install dobot-api keyboard
  ```

3. Ensure the Dobot arm is connected and the necessary drivers are installed on your system. Refer to the Dobot API documentation for more details.

