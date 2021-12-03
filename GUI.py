import tkinter as tk
import Host_discovery
from PIL import Image, ImageTk
win=tk.Tk()
win.title("NetMonk")
logo= Image.open('/home/yashaskm11/Netmonk/Netmonk.ico')
logo= ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0,row=1)
win.geometry('1920x1080')
c= tk.Canvas(win,bg="gray16",height=200,width=200)
fl=tk.Label(win,image=logo)
fl.place(x=0,y=0,relheight=0,relwidth=0)
win.config(bg="grey")
win.mainloop()
