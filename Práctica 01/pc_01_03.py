total_cuenta = 200.0       # Soles
porcentaje_propina = 15.0  # %
num_personas = 2           # Personas

# Cálculos
propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + propina
monto_persona = total_con_propina / num_personas

# Mostrar resultados
print("--- Calculadora de Propinas ---")
print(f"Total cuenta: S/. {total_cuenta:.2f}")
print(f"Propina ({porcentaje_propina}%): S/. {propina:.2f}")
print(f"Total con propina: S/. {total_con_propina:.2f}")
print(f"Cada persona paga: S/. {monto_persona:.2f}")

# Advertencia
if monto_persona > 100:
    print("¡Atención! Monto por persona supera S/. 100")
else:
    print("El monto por persona es aceptable")