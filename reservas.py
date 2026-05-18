reservas = []

def crear_reserva(nombre, fecha, hora):
    reserva = {
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora
    }
    reservas.append(reserva)

def ver_reservas():
    return reservas