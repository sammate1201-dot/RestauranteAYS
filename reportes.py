def generar_reporte(pedidos):
    total = sum(p["precio"] for p in pedidos)
    print("Total de ventas:", total)