class Sintaxis:
    instancia=0
    
    def __init__ (self,dato="llamando al constructor1"):
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
        materias[1]="Python"
        materias.append("Go")
        docente={}
        docente={'nombres':'Daniel', 'edad':50,'fac':'faci'}
        print("""Mi nombre es {}, tengo {}
                años""".format(nombres ,edad))   


ejer1 = Sintaxis()
ejer1.usoVariables()

