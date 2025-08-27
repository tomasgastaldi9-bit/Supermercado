from models.carrito import Carrito
from models.producto import Producto
import utils.db_utils as db

class Cliente:
    id_cliente: int
    nombre: str
    direccion: str
    carrito: Carrito

    def __init__(self, id_cliente: int, nombre: str, direccion: str = ""):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = Carrito()

    def __str__(self):
        carrito_str = str(self.carrito) if len(self.carrito) > 0 else "Carrito vacío"
        return f"Cliente: {self.nombre} | Dirección: {self.direccion}\nCarrito:\n{carrito_str}"

    def agregar_al_carrito(self, producto: Producto, cantidad: int):
        if producto.hay_stock(cantidad):
            exito, msg = producto.actualizar_stock(-cantidad)
            if exito:
                self.carrito.agregar_producto(producto, cantidad)
            return exito, msg
        else:
            return False, f"No hay suficiente stock de {producto.nombre}."

    def pagar(self):
        if not self.carrito.productos:
            print("El carrito está vacío.")
            return False

        for producto, cantidad in self.carrito.productos:
            # Registrar compra en la DB
            db.registrar_compra(self.id_cliente, producto.codigo, cantidad)
            # Actualizar stock en la DB
            db.actualizar_stock(producto.codigo, cantidad)

        self.carrito.vaciar_carrito()
        print("✅ Compra registrada y pagada con éxito.")
        return True