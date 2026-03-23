from trabalho import calcular_total, validar_pedido


def test_calcular_total_simples():
    assert calcular_total(10, 2) == 20


def test_validar_pedido_valido():
    assert validar_pedido(5, 3) is True