class Ordenar:
    def _init_(self,lista):
         self.lista=lista
        
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    def recorrerPosicion(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)

    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])


lista = [2,3,1,5,8,10]
Ord1 = Ordenar(lista)
Ord1.recorrerRange()
