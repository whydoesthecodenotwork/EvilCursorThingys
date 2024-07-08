import socket
import threading

def handle_client(client_socket):
  while True:
    data = client_socket.recv(1024)
    # user absolutely EXPLODED
    if not data:
      break
    message = data.decode('utf-8')
    print(f"Received message: {message}")
    response = "Server received your message: " + message
    client_socket.sendall(response.encode('utf-8'))
  client_socket.close()