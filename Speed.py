import datetime
import os
import time
import GUI
import gfiberspeedtest
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='test'
)
mycursor = mydb.cursor(buffered=True)
#st=speedtest.Speedtest()

global Threadflag
Threadflag=True


def SpeedmonkeyT():
    while Threadflag:
        Speedmonkey()


def Speedmonkey():
    output = os.popen('speedtest-cli')
    i=0
    while True:
        line = output.readline()
        i+=1
        if line:
            if i==7:
                dl=line
            elif i==9:
                ul=line
            #print(line,i, end='')
        else:
            break

    output.close()
    dl = extract(dl)
    ul = extract(ul)
    timestamp = datetime.datetime.now()
    pushspeed((ul, dl, timestamp))
    time.sleep(20)

def pushspeed(val):
    sql="insert into speedmonk values (%s,%s,%s)"
    mycursor.execute(sql,val)
    mydb.commit()

def extract(st):
    fl=''
    num=['1','2','3','4','5','6','7','8','9','0','.']
    for i in st:
        if i in num:
            if i=='.':
                if not fl=='':
                    fl=fl+i
            else:
                fl=fl+i
    return float(fl)

def Threadtoggle():
    global Threadflag
    if GUI.flag.get():
        Threadflag = True
       # t1.start()
    else:
        Threadflag=False
       # t1.join()

