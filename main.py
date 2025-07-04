from operaciones_para_negocio import calcular_interes_simple, valor_futuro, convertir_moneda

# Interés simple
capital = 1000
tasa = 0.05
tiempo = 2
print("Interés simple:", calcular_interes_simple(capital, tasa, tiempo))

# Valor futuro
print("Valor futuro:", valor_futuro(capital, tasa, tiempo))

# Conversión de moneda
usd = 100
tasa_cambio = 0.93  # USD a EUR
print("100 USD en EUR:", convertir_moneda(usd, tasa_cambio))
