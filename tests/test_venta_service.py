from venta_service import registrar_venta

def test_registrar_venta():
    resultado = registrar_venta("Arroz Chaufa",2,12)
    assert resultado == True

def test_registro_invalido():
    resultado = registrar_venta("Ceviche",0,15)
    assert resultado == False    