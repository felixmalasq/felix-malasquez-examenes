#EJERCICIO 3 - Crear la función de normalizar_telefonos(numeros, pais_defecto) la
#cual para sus parámetros tendrá las siguientes especificaciones:

def normalizar_telefonos(numeros, pais_defecto):
    codigos_pais = {
        "perú": "+51",
        "argentina": "+54",
        "chile": "+56"
    }

    if pais_defecto not in codigos_pais:
        return {"error, prefijo {} no válido. Ingrese prefijo de perú, argentina o chile".format(pais_defecto)}

    validos = []
    invalidos = ["NO VÁLIDOS"]

    for numero in numeros:
        numero_str = str(numero)