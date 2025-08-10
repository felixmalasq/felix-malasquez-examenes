def normalizar_nombres(nombres):
    nombres_limpios = []

    for nombre in nombres:
        # - Este quitará el espacio antes y después si lo hubiera
        nombre = nombre.strip()

        # - Convierte en tipo título
        nombre = nombre.title()

        # - Devuelve también eliminando duplicados manteniendo el orden de la primera
        if nombre not in nombres_limpios:
            nombres_limpios.append(nombre)

     return nombres_limpios