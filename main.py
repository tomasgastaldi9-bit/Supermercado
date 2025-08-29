from models.producto import Producto
from models.proveedor import Proveedor
from models.cliente import Cliente
import utils.db_utils as db
import sqlite3

DB_NAME = "supermercado.db"

# --- Cargar productos desde la DB ---
productos = []
for fila in db.ver_productos():
    codigo, nombre, precio, stock = fila
    productos.append(Producto(codigo, nombre, precio, stock))

# --- Crear proveedor (con productos cargados) ---
proveedor = Proveedor(1, "SuperProveed", "123456789", "Calle Falsa 123", productos)

# --- Crear o recuperar cliente ---
cliente_id = 1
db.agregar_cliente(cliente_id, "Tomas", "Calle Falsa 123")  # agrega si no existe

# Recuperar datos del cliente para crear el objeto Cliente
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute("SELECT * FROM clientes WHERE id_cliente = ?", (cliente_id,))
fila = cursor.fetchone()
conn.close()

if fila:
    cliente = Cliente(*fila)
else:
    print("No se encontró el cliente en la DB.")
    exit()

# --- Función para mostrar productos disponibles ---
def mostrar_productos():
    print("\nProductos disponibles:")
    for p in productos:
        print(f"{p.codigo} - {p.nombre} | Precio: {p.precio} | Stock: {p.stock}")

# --- Menú interactivo ---
while True:
    print("\n--- MENÚ SUPERMERCADO ---")
    print("1. Agregar producto al carrito")
    print("2. Ver carrito")
    print("3. Pagar")
    print("4. Listar productos del proveedor")
    print("5. Vaciar carrito")
    print("6. Eliminar producto del carrito")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            mostrar_productos()
            try:
                codigo = int(input("Ingrese el código del producto: "))
                cantidad = int(input("Ingrese la cantidad: "))
            except ValueError:
                print("Cantidad o código inválido. Debe ser un número entero.")
            else:
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a cero.")
                else:
                    producto_seleccionado = next((p for p in productos if p.codigo == codigo), None)
                    if producto_seleccionado:
                        exito, msg = cliente.agregar_al_carrito(producto_seleccionado, cantidad)
                        print(msg)
                    else:
                        print("Producto no encontrado.")

        case "2":
            if cliente.carrito.productos:
                print("\nCarrito actual:")
                print(cliente.carrito)
            else:
                print("El carrito está vacío.")

        case "3":
            if cliente.carrito.productos:
                cliente.pagar()  # Aquí se registran compras y se actualiza stock
            else:
                print("El carrito está vacío.")

        case "4":
            print("\nProductos del proveedor:")
            proveedor.listar_productos()

        case "5":
            if cliente.carrito.productos:
                cliente.carrito.vaciar_carrito()
                print("Carrito vaciado correctamente.")
            else:
                print("El carrito está vacío.")

        case "6":
            if cliente.carrito.productos:
                print("\nCarrito actual:")
                print(cliente.carrito)
                cod = int(input("Digite el código del producto que desea eliminar: "))
                existia = any(p.codigo == cod for p, c in cliente.carrito.productos)
                cliente.carrito.productos = [(p, c) for (p, c) in cliente.carrito.productos if p.codigo != cod]
                print("Producto eliminado." if existia else "No existe producto con ese código.")
            else:
                print("El carrito está vacío.")

        case "7":
            print("¡Gracias por usar el supermercado! Hasta luego.")
            break

        case _:
            print("Opción inválida, intente nuevamente.")

