from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

def generate_qrcode():
  link_name = name_input.get()
  link = link_input.get()
  file_name = link_name + ".png"
  url = pyqrcode.create(link)
  url.png(file_name, scale=6)
  image = ImageTk.PhotoImage(Image.open(file_name))
  image_label = Label(image=image)
  image_label.image = image
  canvas.create_window(200, 420, window=image_label)
  

root = Tk()

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text='QR Code Generstor', fg='blue', font=('Arial', 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text='Link name')
name_input = Entry(root)
link_label = Label(root, text='Link')
link_input = Entry(root)
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 130, window=name_input)
canvas.create_window(200, 160, window=link_label)
canvas.create_window(200, 180, window=link_input)

button = Button(root, text='Generate QR code', command=generate_qrcode)
canvas.create_window(200, 230, window=button)


root.mainloop()