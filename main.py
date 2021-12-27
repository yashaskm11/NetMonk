import tkinter as tk
import GUI
import threading
import speedtest
import mysql.connector
import datetime
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(speed())
    #t1=threading.Thread(target=GUI.Gui)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
