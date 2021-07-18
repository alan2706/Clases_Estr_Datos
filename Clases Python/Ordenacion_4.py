class ordenar:
    def _init_(self,lista):
        self.lista=lista

    def ordenarAsce(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista [pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux


lista = [2,3,1,5,8,10]
ord1 = ordenar(lista)
print(ord1.lista)
ord1.ordenarAsce()
print(ord1.lista)

