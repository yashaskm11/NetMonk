import datetime
import speedtest
import threading
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='test'
)
mycursor = mydb.cursor(buffered=True)
st=speedtest.Speedtest()


def pushspeed(val):
    sql="insert into speedmonk values (%s,%s,%s)"
    mycursor.execute(sql,val)
    mydb.commit()

def SpeedT():
    while True:
        val=speed()
        pushspeed(val)


def speed():
    ul=st.upload()
    dl=st.download()
    ul = round(ul / (1e+6), 2)
    dl = round(dl / (1e+6), 2)
    timestamp = datetime.datetime.now()
    return (ul,dl,timestamp)

SpeedT()
print("Speedtest Daemon Started Successfully")

