import mysql.connector
from ping3 import ping
from itertools import count
import time
import datetime
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

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
#fig=plt.figure()
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
    pinging('192.168.0.161')
    mycursor.execute('Select res,time from pingtime where ip=(%s)', ('192.168.0.161',))
    resp = mycursor.fetchall()

    res.append(float(resp[i][0]))
    # dates.append((i[1]))
    lis.append(resp[i][1])
    plt.cla()
    plt.plot(lis, res)
    # print(resp[i][0])
    i += 1


mycursor.execute('truncate pingtime')
ani = animation.FuncAnimation(plt.gcf(), animate, interval='5000')
plt.tight_layout()
plt.show()
