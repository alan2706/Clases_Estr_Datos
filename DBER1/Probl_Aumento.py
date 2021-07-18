class aumento:
    def __init__(self):
        pass
    def aumento_del_sueldo(self):
        Sueldo = float(input("ingrese el sueldo:"))
        if Sueldo >600:
            nsueldo = Sueldo*0.10
            totalsueldo = nsueldo + Sueldo
            print("El nuevo sueldo es de:{}".format(totalsueldo))
        else:
            sueldo1 = Sueldo
            print("El sueldo es de:{} ".format(sueldo1))

tarea=aumento()
tarea.aumento_del_sueldo()

