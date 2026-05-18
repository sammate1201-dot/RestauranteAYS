pedidos = []

def crear_pedido(cliente, producto, precio):
    pedido = {
        "cliente": cliente,
        "producto": producto,
        "precio": precio,
        "estado": "pendiente"
    }
    pedidos.append(pedido)

def ver_pedidos():
    return pedidos