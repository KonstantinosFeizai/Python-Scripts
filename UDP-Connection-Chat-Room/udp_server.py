import socket
import threading
import queue

# Queue to store incoming messages
messages=queue.Queue()
# List to keep track of connected clients
clients=[]

# Create a UDP socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Bind the server to localhost on port 9999
server.bind(("localhost",9999))

# Function to receive messages from clients
def receive():
    while True:
        try:
             # Receive message and sender address
            message,addr=server.recvfrom(1024)
            # Put the message and address into the queue
            messages.put((message,addr))
        except:
            pass  # Ignore any errors


# Function to broadcast messages to all clients
def broadcast():
    while True:
        while not messages.empty():
            message,addr=messages.get()
            print(message.decode()) # Print received message to the server console

             # If the sender is new, add them to the clients list
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    # Check if the message is a signup message (new user joining)
                    if message.decode().startswith("SIGNUP_TAG:"):
                         # Extract the username from the signup message
                        name=message.decode()[message.decode().index(":")+1:]
                        # Notify all clients that a new user has joined
                        server.sendto(f"{name} Joined!".encode(),client)
                    else:
                        # Forward the received message to all clients
                        server.sendto(message,client)
                except:
                    # Remove any client that causes an error (e.g., disconnected client)
                    clients.remove(client)

# Create two threads for receiving and broadcasting messages
t1=threading.Thread(target=receive)
t2=threading.Thread(target=broadcast)

# Start the threads
t1.start()
t2.start()