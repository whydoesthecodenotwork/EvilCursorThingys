import mouse
import win32gui, win32con
shapes = []

pos = (0,0)
def get_position():
  pos = mouse.get_position()
  for rect in shapes:
    canvas.coords(rect, pos[0]-10, pos[1]-10, pos[0]+10, pos[1]+10)

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

shapes.append(canvas.create_rectangle(0, 0, 0, 0,outline="blue", fill="blue"))
shapes.append(canvas.create_rectangle(0, 0, 0, 0,outline="red", fill="red"))
shapes.append(canvas.create_rectangle(0, 0, 0, 0,outline="green", fill="green"))

root.update()
hwnd = win32gui.FindWindow(None, "evilcursorthing")
l_ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
l_ex_style |= win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, l_ex_style)

while True:
  root.update()
  get_position()