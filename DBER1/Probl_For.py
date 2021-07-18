class forrepeticion:
    def __init__(self):
        pass
    def Ciclo_For(self):
        Suma,n,i=0,0,0
        for i in range(100):
            suma=suma+i*i
            print ("el contador es:{} la suma es:{}".format(i,Suma))
tarea=forrepeticion()
tarea.Ciclo_For()
