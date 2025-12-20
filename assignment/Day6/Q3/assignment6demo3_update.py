import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="sensor_datas"
)

cursor = db.cursor()

id = int(input("Enter ID to update: "))
new_temp = float(input("Enter new temperature: "))

sql = "UPDATE temperature_readings SET temperature=%s WHERE id=%s"
cursor.execute(sql, (new_temp, id))
db.commit()

print("Temperature updated successfully")

cursor.close()
db.close()
