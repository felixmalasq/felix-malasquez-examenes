# Asignar en variables los datos de tu nombre, salario, edad y compañia para un usuario
nombre = "Felix Malasquez"
salario = 3000.00
edad = "35"  #Tipo string
compania = "yohama"

# Identificación de tipos de variables
print(f"Tipo de variable 'nombre': {type(nombre)}")
print(f"Tipo de variable 'salario': {type(salario)}")
print(f"Tipo de variable 'edad': {type(edad)}")
print(f"Tipo de variable 'compania': {type(compania)}")

# Conversión de edad a entero
edad_int = int(edad)

# Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted tiene un bono del 5% en el mes diciembre”
if edad_int > 30:
    mensaje = "Usted tiene un bono de 10% en el mes de diciembre"
    porcentaje_bono = 0.10
else:
    mensaje = "Usted tiene un bono del 5% en el mes diciembre"
    porcentaje_bono = 0.05

print(mensaje)

# Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su salario, según corresponda.
bono_final = (salario ** 2) + (salario * porcentaje_bono)
print(f"El bono final es: {bono_final:.2f}")