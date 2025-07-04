def calcular_interes_simple(capital, tasa, tiempo):
    """
    Calcula el interés simple.
    :param capital: Monto inicial
    :param tasa: Tasa de interés anual (ej. 0.05 para 5%)
    :param tiempo: Tiempo en años
    :return: Interés simple
    """
    return capital * tasa * tiempo

def valor_futuro(capital, tasa, tiempo):
    """
    Calcula el valor futuro con interés simple.
    :param capital: Monto inicial
    :param tasa: Tasa de interés anual
    :param tiempo: Tiempo en años
    :return: Monto total al final del período
    """
    return capital * (1 + tasa * tiempo)
