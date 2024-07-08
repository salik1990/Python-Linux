import threading
from tcp_server import start_tcp_server
from uart_listener import start_uart_listener

if __name__ == "__main__":
    try:
        # Start TCP server in a separate thread
        tcp_thread = threading.Thread(target=start_tcp_server, daemon=True)
        tcp_thread.start()
        print("TCP server thread started.")

        # Start UART listener in a separate thread
        uart_thread = threading.Thread(target=start_uart_listener, args=('/dev/ttyS10', 9600), daemon=True)
        uart_thread.start()
        print("UART listener thread started.")

        # Keep the main thread alive to let TCP and UART threads run
        while True:
            pass

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        print("Exiting...")
        # Optionally, you can add cleanup code here if needed
