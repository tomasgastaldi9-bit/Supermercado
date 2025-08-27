from models.producto import Producto

class Proveedor:
    id: int
    nombre: str
    telefono: str
    direccion: str
    productos: list[Producto]

    def __init__(self, id: int, nombre: str, telefono: str, direccion: str, productos: list[Producto]):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.productos = list(productos)

    def __str__(self) -> str:
        return f'Proveedor: {self.nombre} | Telefono: {self.telefono} | Direccion: {self.direccion}'

    def abastecer_productos(self, producto: Producto, cantidad: int) -> tuple[bool, str]:
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor a 0."
        if producto not in self.productos:
            return False, f'{self.nombre} no provee {producto.nombre}.'
        producto.stock += cantidad
        return True, f'{producto.nombre} abastecido con {cantidad} unidades exitosamente.'

    def listar_productos(self):
        print(*self.productos, sep="\n")