from models.producto import Producto

class Carrito:
    def __init__(self):
        self.productos: list[tuple[Producto, int]] = []

    def __str__(self):
        return "\n".join([f"{producto.nombre} - Cantidad: {cantidad} - Codigo: {producto.codigo}"
                          for producto, cantidad in self.productos])

    def __len__(self):
        return len(self.productos)

    def __iter__(self):
        return iter(self.productos)

    def agregar_producto(self, producto: Producto, cantidad: int):
        for i, (p, c) in enumerate(self.productos):
            if p == producto:
                self.productos[i] = (p, c + cantidad)
                return
        self.productos.append((producto, cantidad))

    def vaciar_carrito(self):
        self.productos.clear()