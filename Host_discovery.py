import mysql.connector
from ping3 import ping
from itertools import count
import time
import datetime
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
#figure=plt.Figure()
global IP
def globvar():
    global resp
    resp=list()
mydb = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='test'
)
mycursor = mydb.cursor()
dates = []
res = []
lis = []
index = count()
style.use('fivethirtyeight')
#ax1=fig.sub_plots(1,1,1)


def pinging(ip):
    res = ping(ip, unit='ms')
    timestamp = datetime.datetime.now()
    pushtodb((ip, res, timestamp))


def pushtodb(val):
    sql = "INSERT INTO pingtime VALUES (%s,%s,%s)"
    mycursor.execute(sql, val)
    mydb.commit()


flag = True


def animate(i):
    # time.sleep(1)

    if i==0:
        global lis,res
        res=list()
        lis=list()

    pinging(IP)
    mycursor.execute('Select res,time from pingtime where ip=(%s)', (IP,))
    resp = mycursor.fetchall()

    res.append(float(resp[i][0]))
    # dates.append((i[1]))
    lis.append(resp[i][1])
    plt.cla()
    plt.plot(lis, res)
    # print(resp[i][0])
    i += 1

def start(ip):
    IP=ip
    mycursor.execute('truncate pingtime')
    #plt.cla()
    #plt.title("Monitoring ")
    ani = animation.FuncAnimation(plt.gcf(), animate, interval='5000')
    #fig = plt.figure()
    plt.tight_layout()
    plt.show()
