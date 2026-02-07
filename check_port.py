import socket
import sys
import time

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result == 0

port = int(sys.argv[1])
print(f"Checking port {port}...")
for i in range(10):
    if check_port(port):
        print(f"SUCCESS: Port {port} is listening.")
        sys.exit(0)
    time.sleep(1)
    print(f"Waiting... ({i+1}/10)")

print(f"FAILURE: Port {port} is NOT listening.")
sys.exit(1)
