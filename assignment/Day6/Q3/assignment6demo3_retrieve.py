import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="sensor_datas"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM temperature_readings")
records = cursor.fetchall()

print("ID | Temperature | Date-Time")
for row in records:
    print(row)

cursor.close()
db.close()