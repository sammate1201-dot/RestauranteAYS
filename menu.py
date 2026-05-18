menu = {}

def agregar_producto(nombre, precio):
    menu[nombre] = precio

def ver_menu():
    return menu

def actualizar_producto(nombre, precio):
    if nombre in menu:
        menu[nombre] = precio

def eliminar_producto(nombre):
    if nombre in menu:
        del menu[nombre]