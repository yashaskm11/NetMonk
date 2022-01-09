import tkinter as tk
from tkinter import *

import Host_discovery
import SSHClient
import mysql.connector
import multiprocessing
import threading
import datetime
import nmap3
import SpeedAPI
import speedmonk

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

def avg(tflag):
    while tflag():
        calavg()

def calavg():

    mydb11 = mysql.connector.connect(
        host="localhost",
        user='yashaskm11',
        password='4747',
        database='Netmonk'
    )
    mycursor11 = mydb11.cursor()
    val = datetime.date.today()
    mycursor11.execute("select avg(download) from speedmonk where DATE(time)= (%s) ",(val,))
    davg=mycursor11.fetchone()
    mycursor11.execute("select avg(upload) from speedmonk where DATE(time) = (%s) ",(val,))
    uavg=mycursor11.fetchone()
    st="Download : "+str(round(davg[0],2))+" Upload : "+str(round(uavg[0],2))
    global tflag
    if tflag:
        v11.set(st)

def start():
    host=sel_ip.get()
    if host=='':
        can.itemconfigure(can10, state='normal')
        return
    else:
        can.itemconfigure(can10, state='hidden')
    Host_discovery.IP=sel_ip.get()
    Host_discovery.start(host)

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
    win1.iconbitmap(r"Images/net-rt.ico")
    win1.geometry('350x250+1100+300')
    para=tk.StringVar()
    por=tk.Label(win1, textvariable=para)
    por.pack()
    nm=nmap3.NmapHostDiscovery()
    res=nm.nmap_portscan_only(host)
    li=res[host]
    hostname=li['hostname']
    lis=li['ports']
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
    par=par+"\n-------END OF LIST-------"
    para.set(par)
    if g:
        ssh.pack()

def scan():
    nmap = nmap3.NmapHostDiscovery()
    l1 = list()
    results = nmap.nmap_no_portscan("192.168.0.0/24")
    pr=50
    for i in results:
        pr+=1
        if not(i=='runtime' or i=='stats'):
            l1.append(i)
    can.create_text(300,400,anchor="nw",text="Select any IP :",font=("Product Sans",20),fill="white")
    op = tk.OptionMenu(frame1, sel_ip, *l1)
    can5 = can.create_window(500, 400, anchor="nw", window=op,width=150)
    por=tk.Button(frame1,text='Start Port Scan', command=port1,font=("Product Sans",))
    monit = tk.Button(frame1, text='Monitor', command=start,font=("Product Sans",))
    can3 = can.create_window(700, 400, anchor="nw", window=por)
    can6 = can.create_window(900, 400, anchor="nw", window=monit)

win = tk.Tk()
global v11
v11=tk.StringVar()
q=multiprocessing.Queue()
p=threading.Thread(target=SpeedAPI.SpeedProc,args=(q,v11))# Thread 1
p.start()
flag=tk.IntVar()
bg = PhotoImage(file="Images/Netmonk.png")
scan_img=PhotoImage(file="Images/SCAN.png")
global can10
frame1=tk.Frame(win).pack()
sel_ip=tk.StringVar()
win.title("NetMonk")
win.iconbitmap(r"Images/net-rt.ico")
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
can.create_text(585,20,anchor="nw",text="Average Internet Speeds",font=("Product Sans",14))
av=tk.Label(frame1,textvariable=v11,bg='green')
can.create_window(605,50,anchor="nw",window=av)
can.itemconfigure(can10,state='hidden')
can1=can.create_window(1100,500,anchor="nw",window=tog)
can2=can.create_window(80,400,anchor="nw",window=scan)
win.mainloop()
q.put(0)
print("Waiting for Background Processes to Close")
p.join()
print("Thread Closed\nGoodbye !")
