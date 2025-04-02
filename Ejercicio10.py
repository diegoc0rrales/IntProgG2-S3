radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

pi=3.1416
area_base = pi * (radio ** 2)

volumen = area_base * altura

area_lateral = 2 * pi * radio * altura

area_superficial = area_lateral + (2 * area_base)

print(f"\nRadio ingresado: {radio}")
print(f"Altura ingresada: {altura}")
print(f"Volumen del cilindro: {volumen:.2f}")
print(f"Área superficial del cilindro: {area_superficial:.2f}")