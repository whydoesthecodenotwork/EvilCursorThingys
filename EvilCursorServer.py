# https://pandeyshikha075.medium.com/building-a-chat-server-and-client-in-python-with-socket-programming-c76de52cc1d5

import socket
import threading
import json

clients = {}

def handle_client(client_socket,client_address):
  print(client_address[1])
  clients[client_address[1]] = {"pos": [0,0]}
  while True:
    data = client_socket.recv(1024)
    # user absolutely EXPLODED. exit while loop
    if not data:
      break
    message = data.decode('utf-8')
    print(f"Received message: {message}")
    clients[client_address[1]]["pos"] = message.split(",")
    # response = "Server received your message: " + message
    client_socket.sendall(json.dumps(clients).encode('utf-8'))
  client_socket.close()

def main():
  # ipv4, tcp
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host = '100.101.64.152'
  port = 12345
  server_socket.bind((host, port))
  server_socket.listen(5)
  print(f"Server listening on {host}:{port}")

  while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,client_address,))
    client_handler.start()

if __name__ == "__main__":
  main()