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
   git clone https://github.com/Stax124/DobotAPI.git
   ```
1. Install the required dependencies:

  ```bash
  pip install dobot-api keyboard
  ```

3. Ensure the Dobot arm is connected and the necessary drivers are installed on your system. Refer to the Dobot API documentation for more details.

## Usage

1. Setting Up Coordinates:
Run `coord_init.py` to manually record the arm's coordinates at different positions. This will create or update the `coordinates_for_arm_1.csv` and `coordinates_for_arm_2.csv` files with the current arm positions. You'll need to move the arm to specific points like:

Home position
Pick up position
Pick down position
Place up position
Place down position

2. Running the Dobot Arms:
Once the coordinates are set up, you can run the automation scripts (`arm1.py` and `arm2`.py) to begin the pick-and-place operations. These scripts will use the coordinates from the CSV files and the suction cup effector to automate the task.

Arm 1: Execute `arm1.py` to perform movements based on the coordinates in `coordinates_for_arm_1.csv`.
Arm 2: Execute `arm2.py` to control the second arm based on `coordinates_for_arm_2.csv`.

3. Starting the Server:
The server listens for input from the client and sends commands to the arms accordingly. To run the server:

bash
Copy code
python server.py
This will start the server and allow communication between the client and the arms. The server waits for the client to send a request (e.g., an index), and the arms will execute corresponding actions like moving to specific positions.

4. Monitoring Pose:
To monitor the pose of the robotic arm in real-time, you can run:

```bash
python pose.py
```
This will continuously display the arm's x, y, and z position in the terminal.

Example Interaction
Start the server on the machine connected to the Dobot:

```bash
python server.py
```
Run arm1.py on one machine and arm2.py on another (if using two separate systems).

Send an index number from a client to trigger specific actions. For example, sending 1 will start the pick-and-place sequence on the Dobot arm.

The arms will perform the task, with the suction cup effector picking up and placing objects at predefined coordinates.

Contributing
Feel free to fork the repository, make changes, and submit pull requests. We encourage contributions to improve the functionality of the Dobot automation system.

