import serial
import time
import keyboard

# Set the Bluetooth serial port
bluetooth_port = '/dev/tty.ROVER_19'  # Change this to match your Bluetooth serial port

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

def full_power():
    send_command('F')

def normal_power(command):
    send_command(command)
    print(f"Command sent: {command}")
    time.sleep(0.3)
    send_command('S')

# Function to control the rover
def control_rover():
    while True:
        command = None
        arrow_keys_mapping = {
            "up": "F",
            "down": "B",
            "left": "L",
            "right": "R",
        }


        key_event = keyboard.read_event()
        if key_event.event_type == "down":
            if key_event.name == 'esc':  # Press 's' to stop
                command = 'S'
            elif key_event.name in arrow_keys_mapping:  # Arrow keys mapping
                command = arrow_keys_mapping[key_event.name]
            elif key_event.name == 'space':  # Press 'space' for full power
                full_power()

            if command:
                normal_power(command)

# Main function
if __name__ == "__main__":
    try:
        control_rover()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        bluetooth.close()
