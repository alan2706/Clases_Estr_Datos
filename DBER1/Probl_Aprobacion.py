class Alumno:
    def __init__(self):
        pass
    def calificacion_del_alumno(self):
        cali1 = float(input("ingrese primera calificación:"))
        cali2 = float(input("ingrese segunda calificación:"))
        cali3 = float(input("ingrese tercera calificación:"))
        promedio = (cali1+cali2+cali3)/3
        if promedio >=7 :
            print("Aprobado")
        else:
            print("No logro aprobar")

        print("la primera calificaión es de:{} la segunda calificación es de:{} la tercera calificación es de:{} el promedio es de:{}".format(cali1,cali2,cali3,promedio)) 

tarea=Alumno()
tarea.calificacion_del_alumno()

