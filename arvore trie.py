class No:
    def __init__(self,chave=None,valor=None):
        self.chave = chave
        self.valor = valor
        self.proximo = [None] * 10

class Indice:
    def __init__(self):
        self.__raiz = No()
        self.__contador = 0
        
    def adicionar(self, chave=None, valor=None):
        novoNo = self.__raiz
        for elementos in chave:
            if novoNo.proximo[int(elementos)] is None:
                novoNo.proximo[int(elementos)] = No()
            novoNo = novoNo.proximo[int(elementos)]
        if not novoNo.chave is None:
            novoNo.chave = chave
            return
        novoNo.chave = chave
        novoNo.valor = valor
        self.__contador += 1
                
    def __getitem__(self, chave):
        buscaNo = self.__raiz
        for elementos in chave:
            #print(buscaNo.proximo)
            if buscaNo.proximo[int(elementos)] == None:
                raise keyError
            buscaNo = buscaNo.proximo[int(elementos)]
        if not buscaNo.chave is None:
            return buscaNo.valor
