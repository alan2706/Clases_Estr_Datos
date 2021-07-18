class Superficie:
    def __int__(self):
        pass
    def Calcular_La_Superficie_Del_Circulo(self):
        pi=3.1416
        Radio = float(input("Ingrese el valor del radio: "))
        a = pi*(Radio*Radio)
        print("el radio del circulo es: {} la Superficie es: {}".format(Radio,a))

tarea=Superficie()
tarea.Calcular_La_Superficie_Del_Circulo() 

