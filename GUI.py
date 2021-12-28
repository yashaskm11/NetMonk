import tkinter as tk
from tkinter import *
import Host_discovery
import SSHClient
import mysql.connector
from multiprocessing import Process
import threading
from tkinter.ttk import *
import time
import nmap3
import ssl
import datetime
import speedmonk
from pprint import pprint

from PIL import Image, ImageTk
global l1,host
global sel_ip
global flag
l1=['']


mydb1 = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='test'
)
mycursor1 = mydb1.cursor(buffered=True)


#def Threadtoggle():
#    global Threadflag
#    if flag.get():
#        Threadflag = True
#       # t1.start()
#    else:
#        Threadflag=False
#       # t1.join()


#t1.start()
#t1.join()


def start():
    Host_discovery.IP=sel_ip.get()
    Host_discovery.start(sel_ip.get())
    #temp.IP=sel_ip.get()
    #temp.start(sel_ip.get())
    print("Start")

def port1():
    para = tk.StringVar()
    por = tk.Label(frame1, textvariable=para)
    por.pack()
    par="Hello"
    para.set(par)


def port():
    global par
    win1=Toplevel()
    para=tk.StringVar()
    por=tk.Label(win1, textvariable=para)
    por.pack()
    host=sel_ip.get()
    nm=nmap3.Nmap()
    res=nm.nmap_subnet_scan(host)
    #print("------------------------------")
    #res1=nm.nmap_list_scan(host)
    #pprint(res1)
    #pprint(res)
    li=res[host]
    hostname=li['hostname']

    lis=li['ports']
    #print("------------------------------\n",host,"<-->",hostname)
    #k=2.0
    par="Open Ports on "+str(host)
    for i in lis:
        print(i)
        try:
            j=i['service']
            if j['name'] == 'ssh':
                ssh=tk.Button(win1,text="SSH to Client",command=lambda:SSHClient.SSH(host))
        except:
            j['name']=''
        par=par+"\n"+i['portid']+" <--> "+j['name']
    para.set(par)
    ssh.pack()
    #print("------------------------------")
    #print(lis)
def scan():
    nmap = nmap3.NmapHostDiscovery()
    l1 = list()
    results = nmap.nmap_no_portscan("192.168.0.0/24")
    for i in results:
        if not(i=='runtime' or i=='stats'):
            l1.append(i)
    l2=tk.Label(frame1,text="Select any IP for port Scan")
    l2.pack()
    #l2.grid(column=1,row=2)
    op = tk.OptionMenu(frame1, sel_ip, *l1)
    op.pack()
    #op.grid(column=4, row=2)
    #op.pack()
    por=tk.Button(frame1,text='Start Port Scan', command=port)
    monit = tk.Button(frame1, text='Monitor', command=start)
    #ssh=tk.Button(frame1,text='SSH',command=lambda:SSHClient.SSH(sel_ip.get()))
    por.pack()
    monit.pack()
    #por.grid(column=4,row=5,ipady=10)


#t1=threading.Thread(target=Speed.SpeedmonkeyT)
#t1.start()
win = tk.Tk()
flag=tk.IntVar()
logo = Image.open('./Images/Netmonk.ico')
logo = ImageTk.PhotoImage(logo)

frame1=tk.Frame(win).pack()
sel_ip=tk.StringVar()
win.title("NetMonk")
#win.iconbitmap(r'/home/yashaskm11/PyCharmProjects/NetMonk/Images/netmonk-icocon.ico')

logo_label = tk.Label(image=logo)
logo_label.image = logo
#logo_label.pack()
#logo_label.grid(column=0, row=0)
#win.geometry('1920x1080')
#c = tk.Canvas(win, bg="gray16", height=1080, width=1920)
#c.create_image( 0, 0, image = logo,
#                     anchor = "nw")
#c.pack()
fl = tk.Label(frame1, image=logo)

fl.place(x=0, y=0, relheight=0, relwidth=0)
#fl.pack()
win.config(bg="grey")
#rb= tk.Radiobutton(frame1,name="speedtest Daemon YES",text="Yes",value=1,variable=flag).pack()
#rb= tk.Radiobutton(frame1,name="speedtest Daemon NO",text="No",value=0,variable=flag).pack()
tog=tk.Button(frame1,text="Diagnose",command=Host_discovery.Diagnose).pack()
scan = tk.Button(frame1, text='Scan Network', command=scan)
speed= tk.Button(frame1, text="Monitor Internet Speeds", command=speedmonk.PlotSpeed)


#scan.pack()
#scan.grid(column=4,row=0,ipady=10)
#print(l1)
scan.pack()
speed.pack()
win.mainloop()
