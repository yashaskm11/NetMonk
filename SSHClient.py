import paramiko
from tkinter import messagebox as mb
import tkinter as tk
def SSHAuth(host):
    user=v1.get()
    pas=v2.get()
    print(user,pas)
    try:
        client=paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host,port=22,username=user,password=pas)
        mb.showinfo("SSHClient Info","Connection Established to "+host+"\n Check your Console")
        while True:
            try:
                cmd=input("$>_ ")
                if cmd == 'exit': break
                stdin,stdout,stderr=client.exec_command(cmd)
                print(stdout.read().decode())
            except KeyboardInterrupt:
                break
        print("Connection closed")
        client.close()
    except:
        mb.showerror("SSHClient Error","Authentication Failed")


def SSH(host):
    #par=str(par)
    #win2=tk.Tk()
    win2=tk.Toplevel()
    global v1,v2
    v1=tk.StringVar()
    v2=tk.StringVar()
    e1=tk.Entry(win2,textvariable=v1).grid(column=1,row=0)
    e2 = tk.Entry(win2, textvariable=v2).grid(column=1,row=1)
    l1=tk.Label(win2,text="Username").grid(column=0,row=0)
    l2 = tk.Label(win2, text="Password").grid(column=0,row=1)
    b1=tk.Button(win2,text="Login",command=lambda:SSHAuth(host)).grid(column=1,row=2)
    win2.mainloop()

#st="{'protocol': 'tcp', 'portid': '22', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'ssh', 'method': 'table', 'conf': '3'}, 'scripts': []}"
#SSH('192.168.0.200',st)