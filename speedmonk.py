import mysql.connector
import datetime
#import Speed
import matplotlib.animation as animation
import matplotlib.pyplot as plt


#st=speedtest.Speedtest()
#from matplotlib import style
#import GUI

mydb2 = mysql.connector.connect(
    host="localhost",
    user='yashaskm11',
    password='4747',
    database='test'
)
mycursor2 = mydb2.cursor(buffered=True)
ulist=list()
dlist=list()
datelist=list()


def animate(i):
    #Speed.Speedmonkey()
    sql1="select * from speedmonk"
    mycursor2.execute(sql1)
    mydb2.commit()
    resp=mycursor2.fetchall()
    print(resp[-1])
    #print(ulist)
    if not(datelist[-1]==resp[-1][2]):
        ulist.append(resp[-1][0])
        dlist.append(resp[-1][1])
        datelist.append(resp[-1][2])
    #print(ulist,dlist,datelist)
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

#def SpeedThread():
 #   t1=threading.Thread(target=speedmonkT)
  #  t1.start()
    #t1.join()

def PlotSpeed():
    #Speed.Speedmonkey()
    sql1 = "select * from speedmonk where DATE(time) = (%s)"
    val = datetime.date.today()
    mycursor2.execute(sql1, (val,))
    resp = mycursor2.fetchall()
    ulist.clear()
    datelist.clear()
    dlist.clear()
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
    ani = animation.FuncAnimation(plt.gcf(), animate, interval='5000')
    plt.tight_layout()
    plt.show()



