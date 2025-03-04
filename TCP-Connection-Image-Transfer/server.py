import socket
import os
import time

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5) # Set the server to listen for incoming connections

print("Server is listening...")

while True:
    client_socket, address = s.accept()  # Accept a connection from a client
    print(f" Connection from {address} established.")

    # Send a welcome message
    client_socket.send(b"Welcome to the image transfer server!")

    # Open the image in binary mode
    with open("image.jpg", "rb") as f:
        image_data = f.read()

    # Send file size first (fixed 10-byte header)
    file_size = str(len(image_data)).zfill(10)
    client_socket.send(file_size.encode())

    # Notify that the transfer is starting
    print(" Starting image transfer...")
    start_time = time.time()

    # Send the image data
    client_socket.sendall(image_data)

    end_time = time.time()
    transfer_time = end_time - start_time

    print(f" Image sent successfully in {transfer_time:.10f} seconds!")

    # Close the socket connection
    client_socket.close()
