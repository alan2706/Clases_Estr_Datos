class ejercicio:
    def __init__(self):
        pass

    def parimpar(self,numero):
        if numero % 2 == 0:
            print("{} es par".format(numero))
        else:
            print("{} es inpar".format(numero))

ejer= ejercicio()
num=int(input("ingrese un numero: "))
print("llamada 1")
ejer.parimpar(num)
input()
lista = [3,5,6,8,28]
print("llamada 2")
for num in lista:
    ejer.parimpar(num)
input()
print("llamada 3")
ejer.parimpar(23)



