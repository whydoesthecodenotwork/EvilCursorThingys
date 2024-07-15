# https://pandeyshikha075.medium.com/building-a-chat-server-and-client-in-python-with-socket-programming-c76de52cc1d5

import socket
import threading
import json
from colorsys import hls_to_rgb
import randomcolor
rand_color = randomcolor.RandomColor()

clients = {}
# this is a set. do not send these keys to clients
evil = {"res", "color"}

# https://stackoverflow.com/a/31434038
def without_keys(d, keys):
  return {x: d[x] for x in d if x not in keys}

def handle_client(client_socket,client_address):
  clients[client_address[1]] = {"pos": [0,0], "res": [0,0], "color": rand_color.generate(luminosity='bright')}
  clients[client_address[1]]["ice"] = 0
  while clients[client_address[1]]["ice"] < 40:
    try:
      data = client_socket.recv(1024)

      # user might be dead
      if not data:
        print("Oho no", clients[client_address[1]]["ice"])
        clients[client_address[1]]["ice"]+=1
        print(clients[client_address[1]], clients[client_address[1]]["ice"])
        # explode user if they don't respond good enough
        continue
      
      clients[client_address[1]]["ice"] = 0
      message = data.decode('utf-8')
      
      # user is requesting everyone's data
      if message.startswith('help'):
        message = message[4:].split(";")
        print('a man has fallen into the river in lego city', message)
        clients[client_address[1]]["res"] = message[0].split(",")
        clients[client_address[1]]["pos"] = message[1].split(",")
        client_socket.sendall(json.dumps(clients).encode('utf-8'))
        continue
      
      # user is using
      clients[client_address[1]]["pos"] = message.split(",")
      evil_clients = without_keys(clients, evil)
      client_socket.sendall(json.dumps(evil_clients).encode('utf-8'))
    except Exception as e:
      print("OWWWW", e)
      break
  # it's joever
  print(client_address[1], "died!")
  del clients[client_address[1]]
  print(clients)
  client_socket.close()

def main():
  # ipv4, tcp
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host = '100.101.64.166'
  port = 12345
  server_socket.bind((host, port))
  server_socket.listen(5)
  print(f"Server listening on {host}:{port}")

  def loop():
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,client_address,))
    client_handler.start()
    loop()

  loop()

if __name__ == "__main__":
  main()