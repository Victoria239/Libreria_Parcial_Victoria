import pytest
from libreria.producto import Producto

def test_crear_producto_con_precio_base_valido():
    producto = Producto("Libro", 10000)

    assert producto.nombre == "Libro"
    assert producto.precio_base == 10000


def test_rechazar_producto_con_precio_base_cero():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto("Libro", 0)


def test_rechazar_producto_con_precio_base_negativo():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto("Libro", -5000)


def test_aplicar_descuento_cero_es_valido():
    producto = Producto("Libro", 10000)

    producto.aplicar_descuento(0)

    assert producto.descuento == 0


def test_aplicar_descuento_intermedio_es_valido():
    producto = Producto("Libro", 10000)

    producto.aplicar_descuento(20)

    assert producto.descuento == 20


def test_aplicar_descuento_cuarenta_es_valido():
    producto = Producto("Libro", 10000)

    producto.aplicar_descuento(40)

    assert producto.descuento == 40


def test_rechazar_descuento_mayor_a_cuarenta():
    producto = Producto("Libro", 10000)

    with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%"):
        producto.aplicar_descuento(41)


def test_rechazar_descuento_negativo():
    producto = Producto("Libro", 10000)

    with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%"):
        producto.aplicar_descuento(-1)


def test_calcular_precio_final_sin_descuento():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(0)

    precio_final = producto.calcular_precio_final()

    assert precio_final == 11900


def test_calcular_precio_final_con_descuento_y_luego_iva():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(10)

    precio_final = producto.calcular_precio_final()

    assert precio_final == 10710


def test_precio_final_nunca_es_negativo():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(40)

    precio_final = producto.calcular_precio_final()

    assert precio_final >= 0