temp_F = float(input("Ingresa la Temperattura en Farenheit: "))
temp_C = ((temp_F-32)*5/9)
temp_K = temp_C + 273.15
print(f"Grados Celsius, {temp_C:.2f}")
print(f"Grados Kelvin, {temp_K:.2f}")