salario_bruto = float(input("Ingrese el salario bruto del empleado: "))
impuesto_sobre_renta = salario_bruto * 0.1
seguro_social=salario_bruto * 0.05
fondo_pensiones = salario_bruto * 0.03
descuentos = impuesto_sobre_renta + seguro_social + fondo_pensiones
salario_neto = salario_bruto - descuentos
print(f"El salario bruto del empleado es: {salario_bruto:.2f}")
print(f"Los descuentos equivalen a: {descuentos:.2f}")
print(f"El salario neto del empleado es: {salario_neto:.2f}")