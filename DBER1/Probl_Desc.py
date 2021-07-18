class Descuento:
    def __init__(self):
        pass
    def Calcular_Valor_Descuento_(self):
        descuento = float(input("ingrese valor del descuento: "))
        compra = float(input("ingrese el valor total de la compra: "))
        total = compra*(descuento/100)
        Desc_Total=compra-total
        print("el valor del descuento es del: {}% "  "el valor total de la compra es: {} El valor que debe pagar es: ${}".format(descuento,compra,Desc_Total))
tarea=Descuento()
tarea.Calcular_Valor_Descuento_()  

