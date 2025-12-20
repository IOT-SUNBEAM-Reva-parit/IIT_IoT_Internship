import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="sensor_datas"
)

cursor = db.cursor()

temp = float(input("Enter temperature: "))

sql = "INSERT INTO temperature_readings (temperature) VALUES (%s)"
cursor.execute(sql, (temp,))
db.commit()

print("Temperature record inserted successfully")

cursor.close()
db.close()