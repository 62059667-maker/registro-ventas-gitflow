import sqlite3

def conectar():
    return sqlite3.connect("ventas.db")

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto TEXT,
        cantidad INTEGER,
        precio REAL,
        total REAL,
        fecha TEXT
    )
    """)

    conexion.commit()
    conexion.close()