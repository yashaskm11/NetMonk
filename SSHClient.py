import paramiko
from tkinter import messagebox as mb
import tkinter as tk
def SSHAuth(host):
    us=v1.get()
    pa=v2.get()
    try:
        client=paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host,port=22,username=us,password=pa)
        mb.showinfo("SSHClient Info","Connection Established to "+host+"\n Check your Console")
        while True:
            try:
                commd=input("Netmonk_SSH:"+us+"@"+host+"~ $")
                if commd == 'exit': break
                stdin,stdout,stderr=client.exec_command(commd)
                print(stdout.read().decode())
            except KeyboardInterrupt:
                break
        print("Connection closed")
        client.close()
    except:
        mb.showerror("SSHClient Error","Authentication Failed")


def SSH(host):
    win2=tk.Toplevel()
    win2.title("Netmonk - SSH")
    win2.geometry('+1100+300')
    win2.title("NetMonk")
    win2.iconbitmap(r"Images/net-rt.ico")
    global v1,v2
    v1=tk.StringVar()
    v2=tk.StringVar()
    e1=tk.Entry(win2,textvariable=v1).grid(column=1,row=0)
    e2 = tk.Entry(win2, textvariable=v2,show="*").grid(column=1,row=1)
    l1=tk.Label(win2,text="Username").grid(column=0,row=0)
    l2 = tk.Label(win2, text="Password").grid(column=0,row=1)
    b1=tk.Button(win2,text="Login",command=lambda:SSHAuth(host)).grid(column=1,row=2)
    win2.mainloop()
