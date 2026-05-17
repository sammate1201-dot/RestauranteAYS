menu = {
    "hamburguesa": 15000,
    "pizza": 20000,
    "ensalada": 12000
}

def mostrar_menu():
    print("=== MENÚ ===")
    for producto, precio in menu.items():
        print(f"{producto}: ${precio}")

def tomar_pedido():
    pedido = input("¿Qué deseas pedir?: ")
    if pedido in menu:
        print(f"Tu pedido de {pedido} cuesta ${menu[pedido]}")
    else:
        print("Producto no disponible")

if __name__ == "__main__":
    mostrar_menu()
    tomar_pedido()