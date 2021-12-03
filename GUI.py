import tkinter as tk
import nmap3
from pprint import pprint

from PIL import Image, ImageTk
global l1
global sel_ip
l1=['']

def port():
    host=sel_ip.get()
    nm=nmap3.Nmap()
    res=nm.scan_top_ports(host)
    #pprint(res)
    li=res[host]
    lis=li['ports']
    for i in lis:
        if i['state']=='open':
            j=i['service']
            print(i['portid']+" <--> "+j['name'])
    print("------------------------------")
    #print(lis)
def scan():
    nmap = nmap3.NmapHostDiscovery()
    l1 = list()
    results = nmap.nmap_no_portscan("192.168.0.0/24")
    for i in results:
        if not(i=='runtime' or i=='stats'):
            l1.append(i)
    l2=tk.Label(win,text="Select any IP for port Scan")
    l2.grid(column=1,row=2)
    op = tk.OptionMenu(win, sel_ip, *l1)
    op.grid(column=4, row=2)
    #op.pack()
    por=tk.Button(win,text='Start Port Scan',command=port)
    por.grid(column=4,row=5,ipady=10)


win = tk.Tk()
sel_ip=tk.StringVar()
win.title("NetMonk")
logo = Image.open('/home/yashaskm11/Netmonk/Netmonk.ico')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0)
#win.geometry('1920x1080')
c = tk.Canvas(win, bg="gray16", height=200, width=200)
fl = tk.Label(win, image=logo)
fl.place(x=0, y=0, relheight=0, relwidth=0)
#fl.pack()
win.config(bg="grey")

scan = tk.Button(win, text='Scan Network', command=scan)
#scan.pack()
scan.grid(column=4,row=0,ipady=10)
#print(l1)
win.mainloop()
