# Datos de las calificaciones
matematicas = 17
ciencia = 14
historia = 15

# Pesos de cada materia
peso_matematicas = 0.40
peso_ciencia = 0.30
peso_historia = 0.30

# Cálculo de la nota final
nota_final = (matematicas * peso_matematicas) + (ciencia * peso_ciencia) + (historia * peso_historia)
nota_final_redondeada = round(nota_final, 1)

# Evaluación de aprobación
aprobado = nota_final >= 13.0

# Mostrar resultados
print(f"La nota final es: {nota_final_redondeada}")
print(f"¿Aprobado?: {'Sí' if aprobado else 'No'}")
print(f"El estudiante obtuvo una nota final de {nota_final_redondeada} y su estado final es: {'Aprobado' if aprobado else 'Reprobado'}")