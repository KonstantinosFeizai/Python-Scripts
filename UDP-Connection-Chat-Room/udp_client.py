import socket
import threading
import random

# Create a UDP socket for the client
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Bind the client to localhost and a random available port between 8000 and 9000
client.bind(("localhost",random.randint(8000,9000)))

# Ask the user for a nickname
name=input("Nickname:")

# Function to receive messages from the server
def receive():
    while True:
        try:
             # Receive message from the server
            message, _ = client.recvfrom(1024)
              # Decode and print the received message
            print(message.decode())
        except:
            pass   # Ignore any errors to prevent crashes

# Start a separate thread for receiving messages
t=threading.Thread(target=receive)
t.start()

# Send a signup message to the server to announce the new user
client.sendto(f"SIGNUP_TAG: {name}".encode(), ("localhost",9999))

# Loop to continuously send messages
while True:
    message=input("")   # Get user input
    if message == "!q":
        exit() # Exit the program if user types "!q"
    else:
        # Send the message to the server with the sender's name
        client.sendto(f"{name}: {message}".encode(), ("localhost",9999))

