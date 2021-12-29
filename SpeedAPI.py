import speedtest
import datetime
import mysql.connector

mydb31 = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='test'
)
mycursor31 = mydb31.cursor(buffered=True)

def Speedmonk():
    s=speedtest.Speedtest()
    ul=s.upload()
    dl=s.download()
    ul=round(ul/1e+6,2)
    dl = round(dl / 1e+6, 2)
    timestamp = datetime.datetime.now()
    pushspeed((ul, dl, timestamp))

def pushspeed(val):
    sql="insert into speedmonk values (%s,%s,%s)"
    mycursor31.execute(sql,val)
    mydb31.commit()

def SpeedProc(q):
    while q.empty():
        Speedmonk()

Speedmonk()