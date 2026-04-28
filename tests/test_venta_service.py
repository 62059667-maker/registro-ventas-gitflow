from venta_service import registrar_venta, calcular_total_venta

def test_registrar_venta():
    resultado = registrar_venta("Arroz Chaufa",2,12)
    assert resultado == True

def test_registro_invalido():
    resultado = registrar_venta("Ceviche",0,15)
    assert resultado == False

def test_calcular_total_venta():
    resultado = calcular_total_venta(3,10)
    assert resultado == 30

from modelo_orm import Venta

def test_modelo_orm():
    venta = Venta()
    venta.producto = "Ceviche"
    assert venta.producto == "Ceviche"