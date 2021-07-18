class Ordenar:
    def _init_(self,lista):
        self.lista=lista
        
    def recorrerElemento(self):
         for ele in self.lista:
             print(ele)
            
    def recorrerPosicion(self):
         for pos,ele in enumerate(self.lista):
             print(pos,ele)

lista = [2,3,1,5,8,10]
ord1 = Ordenar(lista)
ord1.recorrerElemento()
ord1.recorrerPosicion()