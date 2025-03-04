import socket # Import socket for network communication
import time # Import time for measuring transfer time
import os   # Import os for opening the received image in Windows

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234)) # Connect to the server

welcome_msg = s.recv(1024).decode("utf-8")
print(f"Server: {welcome_msg}")

# Receive file size first
file_size = int(s.recv(10).decode())

print(f"Receiving an image of {file_size} bytes...")

# Start measuring the time taken to receive the image
start_time = time.perf_counter()

image_data = b""

while len(image_data) < file_size:
    packet = s.recv(4096)
    if not packet:
        break
    image_data += packet

# Calculate the transfer time 
end_time = time.perf_counter()
transfer_time = end_time - start_time

# Define the path where the received image will be saved
image_path = "received.jpg" 

with open(image_path, "wb") as f:
    f.write(image_data)

print(f" Image received and saved as '{image_path}' in {transfer_time:.6f} seconds!")

# Automatically Open the Image
os.startfile(image_path) 

# Close the socket connection
s.close()
