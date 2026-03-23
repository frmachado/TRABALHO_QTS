def calcular_total(quantidade, valor_unitario):
    return quantidade * valor_unitario


def validar_pedido(item, quantidade, valor_unitario):
    if not item:
        return "Pedido inválido"
    if quantidade <= 0:
        return "Pedido inválido"
    if valor_unitario <= 0:
        return "Pedido inválido"
    return "Pedido válido"