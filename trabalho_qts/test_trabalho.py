from trabalho import calcular_total, validar_pedido


def test_calcular_total_simples():
    assert calcular_total(10, 2) == 10


def test_validar_pedido_valido():
    assert validar_pedido(5, 3) is True

def test_validar_pedido_item_vazio():
    assert validar_pedido("", 2, 5) == "Pedido inválido"


