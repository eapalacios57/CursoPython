#Importat modulo
import sqlite3

#Conexion
conexion = sqlite3.connect('Pruebas.db')

#Crear Cursor
cursor = conexion.cursor()

#Crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255),"+
"description text,"+
"precio int(255)"
")")
#Guardar Cambios
conexion.commit()

#Insertar muchos productos
productos = [
    ("Ordenador", "Buen PC", 700),
    ("celular", "Buen PC", 500),
    ("Tablet", "Buen PC", 900),
]
cursor.executemany("insert into productos VALUES (null, ?,?,?)", productos)
conexion.commit()

#Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer Porducto', 'Description de mi Producto', 550)")
conexion.commit()

#Listar datos de una tabla
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
print(productos)

print(cursor)
"""
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
print(productos)

#Borrar Registros
cursor.execute("DELETE FROM productos")

#Cerrar conexion 
conexion.close
