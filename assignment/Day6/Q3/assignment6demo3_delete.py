import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="sensor_datas"
)

cursor = db.cursor()

id = int(input("Enter ID to delete: "))

sql = "DELETE FROM temperature_readings WHERE id=%s"
cursor.execute(sql, (id,))
db.commit()

print("Record deleted successfully")

cursor.close()
db.close()