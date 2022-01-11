import speedtest
import datetime
import mysql.connector

mydb31 = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='Netmonk'
)
mycursor31 = mydb31.cursor(buffered=True)


def SpeedProc(q,v11):
    while q.empty():
        Speedmonk()
        if q.empty():
            calavg(v11)


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

#Speedmonk()