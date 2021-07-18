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
        print(usuario[2],nombres[7]) 


ejer1 = Sintaxis()
ejer1.usoVariables()


