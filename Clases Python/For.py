class For:
    def __init__ (self):
        pass
    def usoFor(self):
        true=0
        nombre= "Alan"
        datos=["Alan",20,true]
        numeros=(2,5.6,4,1)
        docente={'nombre':'Alan','edad':20,'fac':'faci'}
        listanotas=[(30,40),(20,40),(50,40)]
        listaalumnos=[{"nombre":"erick","final":70},{"nombre":"Yandy","final":60},{"nombre":"danny","final":90}]
        j=0
        while j<5:
            print("while",j)
            j=j+1
        print()
        for i in range(5):
            print("for",i,end=" ")
        print()
        for i in range(1,5):
            print("for",i,end=" ")
        print()
        for i in range(2,10,2):
            print("for",i,end=" ")
        print()
        for i in range(12,3,-3):
            print("for",i,end=" ")
        print()
        
        lon=len(datos)
        for pos in range(lon):
            print(pos,datos[pos])
        
        lon=len(numeros)
        for pos in range(lon):
            print(pos,numeros[pos])

        for elem in nombre:
            print(elem,end=" ")
       
        for pos, valor in enumerate(datos):
            print(pos,valor,end=" ")

        for clave,valor in docente.items():
            print(clave,valor,end=" ")

        for notas in listanotas:
            print("for externo",notas)
            for nota in notas:
                print(nota,end=" ")
            print("saliendo del for interno")

        print(listanotas)
        for notas in listanotas:
            acum=0
            for nota in notas:
                acum=acum+nota
            print(acum/len(notas),end=" ")
            
        listaalumnos=[{"nombre":"Erick","Final":70},{"nombre":"Yady","Final":60},{"nombre":"Danny","Final":90}]
        print("\nDiccionario de alumnos")
        print(listaalumnos)
        acum=0
        acum=0
        for alumnos in listaalumnos:
            print(alumnos)
            for clave, valor in alumnos.items():
                print(clave,":",valor,type(valor),end=" ")
                if type(valor)== int:
                    acum=acum+valor
            print()
        print("Promedio",acum/3)  
 

bucle=For()
bucle.usoFor()