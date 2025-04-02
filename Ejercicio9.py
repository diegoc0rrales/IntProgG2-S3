pelicula_min=int(input("Ingresa la duración de la película en minutos"))
comercialesprev_min=int(input("Ingresa la duración de los comerciales previos en minutos"))
pausascom_cant=int(input("Ingresa la cantidad de pausas comerciales durante la película"))
pausascom_min=int(input("Ingresa la duración de cada pausa comercial"))
comdurante=pausascom_cant*pausascom_min
tiempo_total = pelicula_min + comercialesprev_min + comdurante
print(f"Duración original de la película: {pelicula_min} minutos")
print(f"Duración total de comerciales: {comercialesprev_min + comdurante} minutos")
print(f"Tiempo total de la proyección: {tiempo_total} minutos")
