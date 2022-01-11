import mysql.connector
import socket
from tkinter import messagebox as mb
from ping3 import ping
from itertools import count
import datetime
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

global IP,IP1
def globvar():
    global resp
    resp=list()
mydb4 = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='Netmonk'
)
mycursor4 = mydb4.cursor()
dates = []
res = []
lis = []
index = count()
style.use('fivethirtyeight')


def pinging(ip):
    res = ping(ip, unit='ms')
    timestamp = datetime.datetime.now()
    pushtodb((ip, res, timestamp))


def pushtodb(val):
    sql = "INSERT INTO pingtime VALUES (%s,%s,%s)"
    mycursor4.execute(sql, val)
    mydb4.commit()


flag = True


def animate(i):
    if i==0:
        global lis,res
        res=list()
        lis=list()
    else:
        plt.cla()
    pinging(IP)
    mycursor4.execute('Select res,time from pingtime where ip=(%s)', (IP,))
    resp = mycursor4.fetchall()
    res.append(float(resp[i][0]))
    lis.append(resp[i][1])
    plt.xlabel("Time")
    plt.ylabel("Resposne time in milliseconds")
    plt.title("Response time of "+str(IP1))
    plt.plot(lis, res)
    i += 1


def start(ip):
    IP1
    IP=ip
    mycursor4.execute('truncate pingtime')
    ani = animation.FuncAnimation(plt.gcf(), animate, interval='5000')
    plt.tight_layout()
    plt.show()

def Diagnose():
    try:
        sock = socket.create_connection(("www.github.com", 80))
        if sock is not None:
            sock.close
            mb.showinfo('Internet Diagnose Tool', 'You are successfully connected to Internet')
    except OSError:
        try:
            sock =socket.create_connection(('8.8.8.8',53))
            if sock is not None:
                mb.showwarning("Internet Diagnose Tool","You are connected to Internet, Check for DNS Issues")
        except:
            mb.showerror("Internet Diagnose Tool","You are not connected to Internet, Check your Router or Contact your ISP")
