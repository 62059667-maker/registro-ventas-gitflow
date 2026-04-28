from database import conectar
from datetime import datetime

def registrar_venta(producto, cantidad, precio):

    if cantidad <= 0 or precio <= 0:
        return False

    try:
        total = cantidad * precio
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO ventas (producto, cantidad, precio, total, fecha)
        VALUES (?, ?, ?, ?, ?)
        """, (producto, cantidad, precio, total, fecha))

        conexion.commit()
        conexion.close()

        return True
    except:
        return False

def obtener_ventas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM ventas")
    datos = cursor.fetchall()

    conexion.close()
    return datos

def eliminar_venta(id_venta):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM ventas WHERE id=?", (id_venta,))
    conexion.commit()
    conexion.close()

def calcular_total():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT SUM(total) FROM ventas")
    total = cursor.fetchone()[0]

    conexion.close()
    return total if total else 0
def actualizar_venta(id_venta, producto, cantidad, precio):
    try:
        total = cantidad * precio

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        UPDATE ventas
        SET producto=?, cantidad=?, precio=?, total=?
        WHERE id=?
        """, (producto, cantidad, precio, total, id_venta))

        conexion.commit()
        conexion.close()

        return True
    except:
        return False