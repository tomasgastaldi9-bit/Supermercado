import sqlite3
from datetime import datetime

DB_NAME = "supermercado.db"

def agregar_producto(codigo, nombre, precio, stock):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO productos VALUES (?, ?, ?, ?)",
                   (codigo, nombre, precio, stock))
    conn.commit()
    conn.close()

def agregar_cliente(id_cliente, nombre, direccion):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO clientes VALUES (?, ?, ?)",
                   (id_cliente, nombre, direccion))
    conn.commit()
    conn.close()

def registrar_compra(id_cliente, codigo_producto, cantidad):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO compras (id_cliente, codigo_producto, cantidad, fecha) VALUES (?, ?, ?, ?)",
                   (id_cliente, codigo_producto, cantidad, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def ver_productos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

def actualizar_stock(codigo_producto, cantidad):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE productos SET stock = stock - ? WHERE codigo = ?",
        (cantidad, codigo_producto)
    )
    conn.commit()
    conn.close()
