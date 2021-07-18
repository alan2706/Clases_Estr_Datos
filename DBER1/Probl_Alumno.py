class alumno:
    def __init__(self):
        pass
    def Calificacion_Del_Alumno(self):
        Calif1 = float(input("ingrese el valor de la primera calificación:"))
        Calif2 = float(input("ingrese el valor de la segunda calificación:"))
        Calif3 = float(input("ingrese el valor de la tercera calificación:"))
        promedio = (Calif1+Calif2+Calif3)/3
        if promedio >=7 :
            print("Aprobado")

        print("La primera calificaión es de:{} La segunda calificación es de:{} La tercera calificación es de:{} el promedio es de:{}".format(Calif1,Calif2,Calif3,promedio)) 

tarea=alumno()
tarea.Calificacion_Del_Alumno()       

