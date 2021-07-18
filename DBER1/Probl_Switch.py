class dados:
    def __init__(self):
        pass
    def Switch(self):
        Respuesta=0
        Num = int(input("ingrese el valor del numero:"))
        v = int(input("ingrese la variable:"))
        if Num == 1:
            Respuesta = 100*v
        elif Num == 2:
            Respuesta = 100**v
        elif Num == 3:
            Respuesta = 100/v
        else :
            Respuesta = 0
        print("la respuesta es:{} el valor es: {} el valor de la variable es: {}".format(Respuesta,v,Num))

tarea=dados()
tarea.Switch()

