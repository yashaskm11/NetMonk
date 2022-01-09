import time
import mysql.connector
import datetime


def avg(r,v11):
    while r.empty():
        calavg(v11)

def calavg(v11):

    mydb11 = mysql.connector.connect(
        host="localhost",
        user='yashaskm11',
        password='4747',
        database='Netmonk'
    )
    mycursor11 = mydb11.cursor()
    val = datetime.date.today()
    mycursor11.execute("select avg(download) from speedmonk where DATE(time)= (%s) ",(val,))
    davg=mycursor11.fetchone()
    mycursor11.execute("select avg(upload) from speedmonk where DATE(time) = (%s) ",(val,))
    uavg=mycursor11.fetchone()
    st="Download : "+str(round(davg[0],2))+" Upload : "+str(round(uavg[0],2))
    try:
        v11.set(st)
    except:
        pass