class comision:
    def __init__(sel):
        pass
    def calcular_comisión(self):
        Descuento = float(input("ingrese el porcentaje del descuento: "))
        venta1 = float(input("ingrese el valor generado de la primera venta: "))
        venta2 = float(input("ingrese el valor generado de la segunda venta: "))
        venta3 = float(input("ingrese el valor generado de la tercera venta: "))
        sueldo_base = float(input("ingrese el sueldo base: ")) 
        Total_De_Ventas = venta1+venta2+venta3
        comision = Total_De_Ventas*(Descuento/100)
        Total_Por_Recibir = sueldo_base+comision
        print("el valor de la primera venta es:{} el valor de la segunda venta es:{} el valor de la tercera venta es:{} el total de las ventas es:{} el valor de la comsision es:{} el total a recibir es de:{}".format(venta1,venta2,venta3,Total_De_Ventas,comision,Total_Por_Recibir))

tarea=comision()
tarea.calcular_comisión()
