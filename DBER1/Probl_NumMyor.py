class numero_mayor:
    def __init__(self):
        pass
    def Mayor_De_Tres(self):
        Num1 = float(input("ingrese el valor del primer número:"))
        Num2 = float(input("ingrese el valor del segundo número:"))
        Num3 = float(input("ingrese el valor del tercer número:"))
        if Num1 > Num2 and Num1>Num3:
            print("numero mayor es :",Num1)
        else:
            if Num2>Num3:
                print("el numero mayor es :",Num2)
            else:
                print("numero mayor es :", Num3)
tarea=numero_mayor()
tarea.Mayor_De_Tres()

