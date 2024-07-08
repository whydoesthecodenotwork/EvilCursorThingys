import mouse
import win32gui, win32con
pos = (0,0)

shapes = []
def draw_shapes():
  canvas.delete('all')
  for key in clients:
    client = clients[key]
    rect = canvas.create_rectangle(0, 0, 0, 0,outline="blue", fill="blue")
    canvas.coords(rect, int(client["pos"][0])-10, int(client["pos"][1])-10, int(client["pos"][0])+10, int(client["pos"][1])+10)

from tkinter import *
root=Tk()
root.title("evilcursorthing")
res_x = root.winfo_screenwidth()
res_y = root.winfo_screenheight()
# to remove the titlebar
root.overrideredirect(True)
# to make the window transparent
root.attributes("-transparentcolor","white")
# set bg to white in order to make it transparent
root.config(bg="white")
# make window to be always on top
root.wm_attributes("-topmost", 1)

canvas = Canvas(bg="white", width=res_x, height=res_y, borderwidth=0, highlightthickness=0)
canvas.pack()

root.update()
hwnd = win32gui.FindWindow(None, "evilcursorthing")
l_ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
l_ex_style |= win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, l_ex_style)

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '100.101.64.152'
port = 12345
client_socket.connect((host, port))

import json

clients = {}

def send_pos():
  global pos
  global clients
  pos = mouse.get_position()
  message = "{},{}".format(pos[0], pos[1])
  client_socket.sendall(message.encode('utf-8'))
  data = client_socket.recv(1024)
  response = data.decode('utf-8')
  print(f"Server response: {response}")
  clients = json.loads(response)

while True:
  root.update()
  draw_shapes()
  send_pos()