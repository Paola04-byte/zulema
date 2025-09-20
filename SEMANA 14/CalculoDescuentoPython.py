# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento en función del monto total y el porcentaje de descuento.
    Retorna el monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal

# 1ra llamada: usando solo el monto total (se aplicará el 10% por defecto)
monto1 = 200
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

print("Compra 1:")
print(f"Monto total: ${monto1:.2f}")
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

# 2da llamada: usando monto total + porcentaje de descuento específico
monto2 = 500
descuento2 = calcular_descuento(monto2, 20)
monto_final2 = monto2 - descuento2

print("Compra 2:")
print(f"Monto total: ${monto2:.2f}")
print(f"Descuento aplicado (20%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
