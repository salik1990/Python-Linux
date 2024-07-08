import serial

def start_uart_listener(port='/dev/ttyUSB0', baudrate=9600):
    """Listen to UART (serial port) and print received data."""
    with serial.Serial(port, baudrate) as ser:
        print(f"UART listener started on {port} at {baudrate} baudrate")
        while True:
            data = ser.readline().decode().strip()
            if data:
                print(f"Received UART data: {data}")
                ser.write(data.encode())
if __name__ == "__main__":
    start_uart_listener()
