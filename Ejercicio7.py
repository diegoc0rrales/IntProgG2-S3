precio_original=float(input("Ingrese el precio original del producto: "))
porcentaje_descuento=float(input("Ingrese el porcentaje de descuento aplicado: "))
descuento=(precio_original*porcentaje_descuento)/100
precio_descuento=precio_original-descuento
iva=float(input("Ingrese el iva del producto: "))
impuestos=(precio_descuento*iva)/100
precio_final=impuestos+precio_descuento
print("El precio original del producto es: ", precio_original)
print("El descuento aplicado es de: ", descuento)
print("El precio con descuento del producto es: ", precio_descuento)
print("El IVA calculado es de: ", impuestos)
print("El precio final es: ", precio_final)