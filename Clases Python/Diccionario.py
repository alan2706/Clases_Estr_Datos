class Sintaxis:
    instancia=0
    def __init__(self,dato="llamando al constructor1"):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1 

    def usoVariables(self):
        edad, peso=50, 70.5
        nombres = 'Daniel Vera'
        Tipo__sexo = 'M'
        civil = True
        usuario=()
        usuario = ('dchiki', '1234', 'Chiki@gmail.com') 
        materias=[]
        materias=['Programación Web', 'PHP', 'POO']
        aux=materias[1]
        materias[1]="Python"
        materias.append("go")
        docente={}
        docente={'nombres':'Daniel', 'edad':50,'activo': True}
        edad=docente['edad']
        docente['edad']=51
        docente['carrera']='IS'
        # print(docente,edad,docente['edad'])
        print(usuario,usuario[0],usuario[0:2],usuario[-1:])
        print(nombres,nombres[0],nombres[0:2],nombres[-1:])
        print(materias,materias[2:],materias[:1],materias[::],materias[-2:1])

ejer1 = Sintaxis()
ejer1.usoVariables()

