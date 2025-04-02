peso_kg = float(input("Ingresa tu peso en Kg: "))
altura_m =float(input("Ingresa tu altura en metros: "))
imc = peso_kg/(altura_m**2)
imc = round(imc, 2)
if imc < 18.5:
    clasificacion= "Bajo Peso"
elif 18.5<= imc <24.9:
    clasificacion = "Peso Normal"
elif 25<= imc <29.9:
    clasificacion = "Sobrepeso"
elif 30<= imc <40:
    clasificacion = "Obesidad"
else:
    clasificacion = "Obesidad mórbida" 
print("El peso ingresado fue: ", peso_kg)
print("La altura ingresada fue: ", altura_m)
print(f"Tu valor de IMC es: ", imc)
print(f"Tu clasificación de IMC es:", clasificacion )

