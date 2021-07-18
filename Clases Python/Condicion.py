class Condicion:

    def __init__(self,num1=5,num2=4):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.numero2
        self.numero3=numero


    def usolf(self):
        print(self.numero3)     

print("instancia de la clase")
cond2= Condicion()
cond1=Condicion(10,20)
cond1=Condicion()
print(cond2.numero3)
cond1.usolf()
print("Gracias por su visita")


