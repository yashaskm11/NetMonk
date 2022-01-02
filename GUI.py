import tkinter as tk
from tkinter import *
import Host_discovery
import SSHClient
import mysql.connector
import multiprocessing
from multiprocessing import Process
import threading
from tkinter import ttk
import time
import nmap3
import SpeedAPI
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
    database='Netmonk'
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
    host=sel_ip.get()
    if host=='':
        can.itemconfigure(can10, state='normal')
        return
    else:
        can.itemconfigure(can10, state='hidden')
    Host_discovery.IP=sel_ip.get()
    Host_discovery.start(host)
    #temp.IP=sel_ip.get()
    #temp.start(sel_ip.get())
    #print("Start")

def port1():
    t2=threading.Thread(target=port)
    t2.start()


def port():
    host=sel_ip.get()
    if host=='':
        can.itemconfigure(can10, state='normal')
        return
    else:
        can.itemconfigure(can10, state='hidden')
    win1=Toplevel()
    win1.title("Netmonk - Scanned Ports")
    win1.geometry('+1100+300')
    para=tk.StringVar()
    por=tk.Label(win1, textvariable=para)
    por.pack()

    nm=nmap3.NmapHostDiscovery()
    #res=nm.nmap_subnet_scan(host)
    #print("------------------------------")
    res=nm.nmap_portscan_only(host)
    #pprint(res)
    #print(res)
    li=res[host]
    hostname=li['hostname']

    lis=li['ports']
    #print("------------------------------\n",host,"<-->",hostname)
    #k=2.0
    par="Open Ports on "+str(host)
    g=0
    for i in lis:
        try:
            j=i['service']
            if j['name'] == 'ssh':
                g=1
                ssh=tk.Button(win1,text="SSH to Client",command=lambda:SSHClient.SSH(host))
        except:
            j['name']='unknown'
        par=par+"\n"+i['portid']+" <--> "+j['name']
    para.set(par)
    if g:
        ssh.pack()
    #print("------------------------------")
    #print(lis)


def scan():
    nmap = nmap3.NmapHostDiscovery()
    l1 = list()
    win3=Toplevel()
    win3.title("Progress")
    pb=ttk.Progressbar(win3,length=100,mode="determinate",orient="horizontal")
    pb.pack()
    pb['value']=25
    results = nmap.nmap_no_portscan("192.168.0.0/24")
    pb['value']=50
    pr=50
    for i in results:
        pb['value']=pr+1
        pr+=1
        if not(i=='runtime' or i=='stats'):
            l1.append(i)
    pb['value']=100
    #win3.mainloop()
    #l2=tk.Label(frame1,text="Select any IP for port Scan")
    can.create_text(300,400,anchor="nw",text="Select any IP :",font=("Product Sans",20),fill="white")
    #l2.pack()
    #l2.grid(column=1,row=2)
    op = tk.OptionMenu(frame1, sel_ip, *l1)
    can5 = can.create_window(500, 400, anchor="nw", window=op,width=150)
    #op.pack()
    #op.grid(column=4, row=2)
    #op.pack()
    por=tk.Button(frame1,text='Start Port Scan', command=port1,font=("Product Sans",))
    monit = tk.Button(frame1, text='Monitor', command=start,font=("Product Sans",))
    #ssh=tk.Button(frame1,text='SSH',command=lambda:SSHClient.SSH(sel_ip.get()))

    can3 = can.create_window(700, 400, anchor="nw", window=por)
    can6 = can.create_window(900, 400, anchor="nw", window=monit)

    #monit.pack()
    #por.grid(column=4,row=5,ipady=10)


#t1=threading.Thread(target=Speed.SpeedmonkeyT)
#t1.start()
q=multiprocessing.Queue()
p=threading.Thread(target=SpeedAPI.SpeedProc,args=(q,))# Threading
#p=multiprocessing.Process(target=Speed.SpeedProc,args=(q,))# Manual method
#p=multiprocessing.Process(target=SpeedAPI.SpeedProc,args=(q,))# API
p.start()
win = tk.Tk()
flag=tk.IntVar()
bg = PhotoImage(file="Images/Netmonk.png")
scan_img=PhotoImage(file="Images/SCAN.png")
global can10
frame1=tk.Frame(win).pack()
sel_ip=tk.StringVar()
win.title("NetMonk")
win.geometry('1280x720')
global can
can=Canvas(win,width=1280,height=720)
can.pack(fill="both",expand=True)
can.create_image(0,0,anchor="nw",image=bg)
tog=tk.Button(frame1,text="Diagnose",command=Host_discovery.Diagnose,font=("Product Sans",))
scan = tk.Button(frame1, text='Scan Network', command=scan,font=("Product Sans",))
speed= tk.Button(frame1, text="Monitor Internet Speeds", command=speedmonk.PlotSpeed,font=("Product Sans",))
can7=can.create_window(80,500,anchor="nw",window=speed)
can10 = can.create_text(450,440,anchor="nw",text="* Please select a IP address",fill="red",font=("Product Sans",12))
can.itemconfigure(can10,state='hidden')
can1=can.create_window(1100,500,anchor="nw",window=tog)
can2=can.create_window(80,400,anchor="nw",window=scan)
win.mainloop()
q.put(0)
print("Waiting for Background Processes to Close")
p.join()