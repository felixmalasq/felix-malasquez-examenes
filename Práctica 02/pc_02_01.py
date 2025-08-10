def procesar_notas(estudiantes:dict):
    final = {}
    mejor_promedio = -1
    mejor_estudiante = ""

    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / 3

        if promedio >= 11:
           estado = "aprobado"
        else:
           estado = "desaprobado"

        final[nombre] = {
                "promedio": promedio,
               "estado": estado
        }

        if promedio > mejor_promedio:
           mejor_promedio = promedio
           mejor_estudiante = nombre

        print("El estudiante con el mejor promedio es {} con {}".format(mejor_promedio, mejor_estudiante))

    return resultados