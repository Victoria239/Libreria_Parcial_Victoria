from behave import given, when, then
from libreria.producto import Producto


@given('existe un producto llamado "{nombre}" con precio base {precio_base:g}')
def step_producto_existente(context, nombre, precio_base):
    context.producto = Producto(nombre, precio_base)
    context.error = None
    context.precio_final = None


@when('aplico un descuento de {descuento:g}')
def step_aplicar_descuento(context, descuento):
    context.producto.aplicar_descuento(descuento)


@when('intento aplicar un descuento de {descuento:g}')
def step_intentar_aplicar_descuento(context, descuento):
    try:
        context.producto.aplicar_descuento(descuento)
    except ValueError as error:
        context.error = str(error)


@when('calculo el precio final')
def step_calcular_precio_final(context):
    context.precio_final = context.producto.calcular_precio_final()


@then('el descuento del producto debe ser {descuento_esperado:g}')
def step_validar_descuento(context, descuento_esperado):
    assert context.producto.descuento == descuento_esperado


@then('el sistema debe mostrar el error "{mensaje}"')
def step_validar_error(context, mensaje):
    assert context.error == mensaje


@then('el precio final debe ser {precio_final_esperado:g}')
def step_validar_precio_final(context, precio_final_esperado):
    assert context.precio_final == precio_final_esperado