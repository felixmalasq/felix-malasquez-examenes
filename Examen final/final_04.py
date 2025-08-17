import datetime
def decorador_hora(func):

    def wrapper(**kwargs):

        ahora = datetime.datetime.now()
        hora = ahora.hour
        minutos = ahora.minute

        print("el decorador está siendo ejecutado a las {} con {} minutos".format(hora, minutos))

        suma = sum(kwargs.values())
        print(f"Suma de los elementos: {suma}")

        resultado = func(**kwargs)

        return resultado

    return wrapper


@decorador_hora
def encontrar_mayor(**numeros):

    if not numeros:
        print("No se proporcionaron números")

    mayor = max(numeros.values())
    print(f"El mayor número es: {mayor}")
    return mayor

# Ejemplos
    print("Ejmplo 1")
    encontrar_mayor(num1=5, num2=10, num3=3, num4=8, num5=2, num6=7)

    print("Ejemplo 2")
    encontrar_mayor(a=15, b=4, c=9, d=12)

    print("Ejemplo 3")
    encontrar_mayor(x=25, y=18, z=30)