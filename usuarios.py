usuarios = {
    "admin": {"password": "123", "rol": "administrador"},
    "mesero1": {"password": "123", "rol": "mesero"},
    "cliente1": {"password": "123", "rol": "cliente"}
}

def login(usuario, password):
    if usuario in usuarios and usuarios[usuario]["password"] == password:
        return usuarios[usuario]["rol"]
    return None
