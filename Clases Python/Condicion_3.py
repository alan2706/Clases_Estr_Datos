class ciclo:

    def __init__(self,num=10):
        self.numero=num


    def usowhile (self):
        print("dentro de la clase",self.numero)
        LETRA=""
        while LETRA not in ("a","e","i","o","u"):
            LETRA =input("ingrese vocal: ").lower()
            #caracter= caracter.lower()

        print("si es la letra correcta:{} si es vocal".format(LETRA))

ciclo1= ciclo()
print("fuera de la clase",ciclo1.numero)
print(ciclo1.usowhile())


