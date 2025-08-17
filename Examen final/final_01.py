class Empleado:
    def __init__(self, nombre, edad, sueldo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = nacionalidad

        def solicitar_nombre(self):
            print("Mi nombre es {}".format(self.nombre))

        def solicitar_edad(self):
            print("Mi edad es {}".format(self.edad))

        def cumpleanos(self):
            self.edad += 1
            print("mi edad es {}".format(self.edad))

        def aumentoSueldo(self):
            aumento = self.sueldo * 0.30
            self.sueldo += aumento
            print("mi nuevo sueldo es {} soles".format(self.sueldo))

        def prediccion(self, ano_futuro, edad_futura):
            if edad_futura < self.edad:
                print("no es posible realizar la operación")

            ano_actual = 2025 # tmb puede ser cualquier otro año
            diferencia_anos = ano_futuro - ano_actual
            edad_calculada = self.edad + diferencia_anos
            print("En el ano {} tendrá {} anos".format(ano_actual, edad_calculada))

class Persona(Empleado):
    def __init__(self, nombre, edad, sueldo, nacionalidad):
        super().__init__(nombre, edad, sueldo)
        self.saldo = sueldo

    def mostrar_saldo(self):
        print("Mi saldo es {}".format(self.saldo))

    def transferencia(self, monto, otro_empleado):
        if self.saldo < monto:
            print("saldo insuficiente")

        self.saldo -= monto
        otro_empleado.saldo += monto
        print("transferencia exitosa. {} / {}".self.mostrar_saldo, otro_empleado.mostrar_saldo)

empleado1 = Empleado("Juan Pérez", 30, 3000, "peruano")
empleado2 = Empleado("María Gómez", 25, 3500, "peruana")
