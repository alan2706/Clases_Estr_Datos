class factorial:
    def Factorial(self):
        numero = int(input("Ingrese el valor del numero: "))
        acu=1
        for Num in range(numero,1,-1):
            acu = acu * Num
        print("numero={} ,factorial={}".format(numero,acu))

tarea = factorial()
tarea.Factorial()

