import mysql.connector

#Conexion a la base de datos
database = mysql.connector.connect(
    host="192.168.0.20",
    user="root",
    passwd="root",
    database="python_master"
)
#Revision si la conexion ha sido correcta
#print(database)
cursor =database.cursor()
"""
#Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS python_master")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
#Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
) 
""")
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)