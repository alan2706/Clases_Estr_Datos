class calificacion:
    def __init__(self):
        pass
    def Exámen_De_Aprueba(self):
        c1 = float(input("ingrese el valor de la primera calificación:"))
        c2 = float(input("ingrese el valor de la segunda calificación:"))
        if c1>=80 and c2>=80:
            print("Aceptado")
        else:
            print("Rechazado")
tarea=calificacion()
tarea.Exámen_De_Aprueba()

