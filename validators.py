# Corrección: manejo mejorado de errores
def validar_producto(producto):
    return producto.strip() != ""

def validar_cantidad(cantidad):
    try:
        return int(cantidad) > 0
    except:
        return False

def validar_precio(precio):
    try:
        return float(precio) > 0
    except:
        return False