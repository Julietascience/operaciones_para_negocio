def convertir_moneda(monto, tasa_cambio):
    """
    Convierte un monto usando una tasa de cambio fija.
    :param monto: Monto a convertir
    :param tasa_cambio: Tasa de conversión (ej. 1 USD = 0.93 EUR → tasa = 0.93)
    :return: Monto convertido
    """
    return monto * tasa_cambio
