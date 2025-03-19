# UDP Chat Application
This is a simple **UDP-based chat application** built using Python's `socket` and `threading` modules. It allows multiple clients to send and receive messages via a server using UDP.

## Features
 Clients can join a chat room by providing a nickname.
 Messages are broadcasted to all connected clients.
 Multi-threaded server for handling multiple clients simultaneously.
 Clients can leave the chat using `!q`.

## How It Works
1. **Server (`udp_server.py`)**  
   - Listens for incoming messages.
   - Manages a list of connected clients.
   - Broadcasts messages to all clients.

2. **Client (`udp_client.py`)**  
   - Sends a "signup" message to notify the server when joining.
   - Runs a separate thread to receive messages.
   - Sends user messages to the server.
   - Exits when `!q` is typed.

   ## How to Run
1. Start the server:  
   ```bash
   python udp_server.py
2. Start one or more clients:
   ```bash
   python udp_client.py
3. Enter a nickname and start chatting!
4. The server must be running before clients can connect.

