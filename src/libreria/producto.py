class Producto:
    def __init__(self, nombre: str, precio_base: float):
        self.nombre = nombre
        self.precio_base = self._validar_precio_base(precio_base)
        self.descuento = 0

    def _validar_precio_base(self, precio_base: float) -> float:
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")
        return precio_base

    def aplicar_descuento(self, descuento: float):
        if descuento < 0 or descuento > 40:
            raise ValueError("El descuento debe estar entre 0% y 40%")

        self.descuento = descuento