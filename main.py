from usuarios import login
from menu import agregar_producto, ver_menu
from pedidos import crear_pedido, ver_pedidos
from reservas import crear_reserva, ver_reservas
from reportes import generar_reporte

# LOGIN
usuario = input("Usuario: ")
password = input("Contraseña: ")

rol = login(usuario, password)

if rol:
    print("Bienvenido, rol:", rol)

    # MENÚ
    agregar_producto("Hamburguesa", 15000)
    agregar_producto("Pizza", 20000)

    print("Menú disponible:", ver_menu())

    # PEDIDO
    crear_pedido(usuario, "Hamburguesa", 15000)

    # RESERVA
    crear_reserva(usuario, "2026-05-20", "7:00 PM")

    print("Pedidos:", ver_pedidos())
    print("Reservas:", ver_reservas())

    # REPORTE
    generar_reporte(ver_pedidos())

else:
    print("Credenciales incorrectas")