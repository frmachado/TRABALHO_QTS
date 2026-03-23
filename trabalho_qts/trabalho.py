def calcular_total(preco, quantidade):
    return preco * quantidade


def validar_pedido(preco, quantidade):
    if preco <= 0:
        return False
    if quantidade <= 0:
        return False
    return True