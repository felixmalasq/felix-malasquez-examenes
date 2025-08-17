import datetime


def conteo(func):

    def wrapper(*args, **kwargs):
        total_parametros = len(args) + len(kwargs)

        if total_parametros <= 1:
            print("Error: La función debe recibir más de 1 parámetro")
            return None

        print(f"La función tiene {total_parametros} parámetros")

        resultado = func(*args, **kwargs)

        print("La función ha sido ejecutada correctamente")
        return resultado

    return wrapper


@conteo
def registrar_alumno(nombre, edad, *notas):

    ahora = datetime.datetime.now()
    hora = ahora.hour
    minutos = ahora.minute

    print("{} de {} años ha sido registrado a las {} horas con {} minutos".format(nombre, edad, hora, minutos))

    if notas:
        promedio = sum(notas) / len(notas)
        print("promedio de notas: {}".format(promedio))
        return promedio
    else:
        print("No se proporcionaron notas")

# ejemplo
    print("Caso correcto (más de 1 parámetro)")
    registrar_alumno("Pedro", 30, 15, 18, 12, 16)

    print("Caso incorrecto (1 parámetro o menos)")
    registrar_alumno("Ana")