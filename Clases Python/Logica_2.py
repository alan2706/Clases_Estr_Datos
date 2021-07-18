class ejercicio:
    def __init__(self):
        pass

    def parimpar(self,numero):
        if numero % 2 == 0:
            print("{} es par".format(numero))
        else:
            print("{} es inpar".format(numero))

    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+1
        if numero == acu:
                print("{} es perfecto".format(numero))
        else:
                print("{} no es perfecto".format(numero))
    
    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+1
        return acu


ejer=ejercicio()
num=int(input("ingrese un numero: "))
print("llamada 1")
resp = ejer.perfecto2(num)
if num == resp:
    print("{} es perfecto".format(num))
else:
    print("{} no es perfecto".format(num))


