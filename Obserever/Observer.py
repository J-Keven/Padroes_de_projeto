class Observador():
    def __init__(self,observado):
        observado.attach(self)
        self.Observado = observado
        
    def __call__(self):
        print("Objeto Observador ativado")
        print("Esta na Hora de Repor o estoque do produto: ")
        self.Observado.Mostrar()
    
class Estque():
    def __init__(self):
        self.__Produto = None
        self.__Quantidade = 0
        self.__QtdMinima = 0
        self.__Observadores = []
    
    def UpdateObservador(self):
        # print(self.__Observadores[0])
        self.__Observadores[0].__call__()
        
     
    @property
    def Produto(self):
        return self.__Produto
    
    @Produto.setter
    def Produto(self, Nome: str):
        self.__Produto = Nome
    
    @property
    def Quantidade(self):
        return self.__Quantidade

    @Quantidade.setter
    def Quantidade(self,Quantidade):
        self.__Quantidade = Quantidade
        
    @property
    def QuantidadeMin(self):
        return self.__QtdMinima

    @QuantidadeMin.setter
    def QuantidadeMin(self,Quantidade):
        self.__QtdMinima = Quantidade
    
    def Mostrar(self):
        print("Nome: ", self.__Produto)
        print("Quantidade em estoque: ", self.__Quantidade)
        
    def Vender(self, qtdVendidos):
        if self.__Quantidade - qtdVendidos >= 0: 
            self.__Quantidade -= qtdVendidos
            print("Venda Realizada")

        if self.__Quantidade <= self.__QtdMinima:
            self.UpdateObservador() #chama o metodo que vai avisar o observador
            
    def attach(self, observer):
        self.__Observadores.append(observer)
    
if __name__ == '__main__':
    print("Iniciou")
    arroz = Estque()
    Mensageiro = Observador(arroz)
    arroz.Produto = 'Arroz'
    arroz.Quantidade = 10
    arroz.QuantidadeMin = 6
    arroz.Vender(1)
    arroz.Vender(1)
    arroz.Vender(1)
    arroz.Vender(1)