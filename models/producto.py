class Producto:
    codigo: int
    nombre: str
    stock: int
    precio: float

    def __init__(self, codigo: int, nombre: str, stock: int, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}'

    def actualizar_stock(self, cantidad: int) -> tuple[bool, str]:
        if cantidad == 0:
            return False, "La cantidad debe ser distinta de 0."

        if cantidad < 0 and abs(cantidad) > self.stock:
            return False, f"No hay suficiente stock para vender {abs(cantidad)} unidades de {self.nombre}. Stock actual: {self.stock}"

        self.stock += cantidad
        return True, f"Stock actualizado de {self.nombre}: {self.stock}"

    def hay_stock(self, cantidad: int = 1) -> bool:
        return self.stock >= cantidad
