import serial
import time
import keyboard

# Set the Bluetooth serial port
# Change this to match your Bluetooth serial port
bluetooth_port = '/dev/tty.ROVER_19'


# Establish serial communication with the Bluetooth module
try:
    bluetooth = serial.Serial(bluetooth_port, 9600, timeout=1)
    print("Bluetooth connection established.")
except serial.SerialException:
    print("Failed to establish Bluetooth connection. Check the port and try again.")
    exit()

# Function to send commands to the rover
def send_command(command):
    bluetooth.write(command.encode())

# Function to activate full power
def full_power():
    send_command('F')
    print("Full power activated.")

# Function to drive the rover at normal power
def normal_power(command):
    send_command(command)
    print(f"Command sent: {command}")
    time.sleep(0.3)
    send_command('S')

# Function to stop the rover
def stop():
    send_command('S')
    print("Rover stopped.")

# Function to rotate the camera
def rotate_camera(position):
    send_command(position)
    print(f"Camera Position: {position}")

# Function to control the rover using the keyboard
def control_rover():
    index = 0
    while True:
        command = None
        arrow_keys_mapping = {
            "up": "F",
            "down": "B",
            "left": "L",
            "right": "R",
        }
        positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        key_event = keyboard.read_event()
        if key_event.event_type == "down":
            if key_event.name == 'esc':  # Press 'esc' to stop
                stop()
            elif key_event.name in arrow_keys_mapping:  # Arrow keys mapping
                command = arrow_keys_mapping[key_event.name]
                normal_power(command)
            elif key_event.name == "command":
                if index < len(positions) - 1:
                    index = index + 1
                else:
                    index = 0
                position = positions[index]
                rotate_camera(position)
            elif key_event.name == 'space':  # Press 'space' for full power
                full_power()


# Main function
if __name__ == "__main__":
    try:
        control_rover()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        bluetooth.close()
