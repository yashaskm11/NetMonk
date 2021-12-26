from os import wait

import speedtest
import speedtestpy
import ssl
import threading
import mysql.connector
import datetime
import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
mydb = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='test'
)
mycursor = mydb.cursor(buffered=True)
ulist=list()
dlist=list()
datelist=list()

def speedmonkT():
    while(True):
        time.sleep(5)
        speedmonk()


def speedmonk():
    st = speedtest.Speedtest()
    try:
        #dl = speedtestpy.data.download()
        ul=st.upload()
        #ul = speedtestpy.data.upload()
        dl=st.download()
    except:
        speedmonk()
    ul = round(ul / (1e+6), 2)
    dl = round(dl / (1e+6), 2)
    timestamp = datetime.datetime.now()
    pushspeed((ul, dl, timestamp))

def pushspeed(val):
    sql="insert into speedmonk values (%s,%s,%s)"
    mycursor.execute(sql,val)
    mydb.commit()

def animate(i):
    sql1="select * from speedmonk order by time DESC"
    mycursor.execute(sql1)
    resp=mycursor.fetchone()
    print(resp)
    print(ulist)
    ulist.append(resp[0])
    dlist.append(resp[1])
    datelist.append(resp[2])
    print(ulist,dlist,datelist)
    plt.cla()
    plt.cla()
    plt.cla()
    plt.plot(datelist,ulist,color='r',label='Upload')
    plt.plot(datelist, dlist, color='b', label='Download')
    plt.xlabel("Time")
    plt.ylabel("Speed in Mbit/sec")
    plt.title("Internet Speed")
    plt.legend()
    print(i)
    i+=1

def SpeedThread():
    t1=threading.Thread(target=speedmonkT)
    t1.start()
    #t1.join()

def PlotSpeed():
    sql1 = "select * from speedmonk where DATE(time) = (%s)"
    val = datetime.date.today()
    mycursor.execute(sql1, (val,))
    resp = mycursor.fetchall()
    for j in resp:
        ulist.append(j[0])
        dlist.append(j[1])
        datelist.append(j[2])
    plt.plot(datelist,ulist,color='r',label='Upload')
    plt.plot(datelist, dlist, color='b', label='Download')
    plt.xlabel("Time")
    plt.ylabel("Speed in Mbit/sec")
    plt.title("Internet Speed")
    plt.legend()
    ani = animation.FuncAnimation(plt.gcf(), animate, interval='10000')
    plt.tight_layout()
    plt.show()
