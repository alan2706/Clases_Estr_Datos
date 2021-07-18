class Tarea:
    def __init__(self):
        pass
    def calcular_jornada_laboral(self):
        ht,he,het = 0,0,0
        ph,phe,pt,ph8 = 0,0,0,0
        ht = int (input("ingrese horaas trabajadas: "))
        ph = float (input ("Ingrese valor hora: "))
        if ht > 40:
            he=ht - 40
            if he > 8:
                het = he - 8
                ph8 = 8 * ph * 2 
                phe = het * ph * 3
            
            else:
                ph8  = he*ph*2   
            pt = 40*ph + ph8 + phe
        else:
             pt = ht * ph
        print("Sobretiempo<8: {} Sobretiempo>8: {} jornada: {} ".format(ph8,phe,pt))    

tarea = Tarea ()
tarea.calcular_jornada_laboral()  

