pesos_amount = 5600
soles_amount = 105
reais_amount = 280
target_amount = 413.0

usd_per_peso = 1 / 18.00
usd_per_soles = 1 / 3.80
usd_per_reais = 1 / 5.00

pesos_in_usd = pesos_amount * usd_per_peso
soles_in_usd = soles_amount * usd_per_soles
reais_in_usd = reais_amount * usd_per_reais



print(f"Pesos in USD: ${pesos_in_usd:.2f}")
print(f"Soles in USD: ${soles_in_usd:.2f}")
print(f"Reais in USD: ${reais_in_usd:.2f}")

print(f"\nComparing to ${target_amount:.2f} USD:")
print(f"Pesos: {'greater than' if pesos_in_usd > target_amount else 'less than or equal to'} ${target_amount:.2f}")
print(f"Soles: {'greater than' if soles_in_usd > target_amount else 'less than or equal to'} ${target_amount:.2f}")
print(f"Reais: {'greater than' if reais_in_usd > target_amount else 'less than or equal to'} ${target_amount:.2f}")


