import sqlite3

def setup_database():
    conn = sqlite3.connect("supermercado.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
        codigo INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        direccion TEXT
    )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS compras (
        id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        codigo_producto INTEGER,
        cantidad INTEGER,
        fecha TEXT,
        FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
        FOREIGN KEY(codigo_producto) REFERENCES productos(codigo)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Base de datos creada correctamente ✅")
