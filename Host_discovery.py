import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user='yashaskm11',
  password='4747',
  database='test'
)

mycursor = mydb.cursor()
sql = "INSERT INTO devices (ip, name) VALUES (%s,%s)"
val = (12, "Yashas", "Beng")
mycursor.execute(sql, val)
mydb.commit()

print(mydb)