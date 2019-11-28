class Singleton():
    __instancia = None
    def __new__(cls,Nome):
        if Singleton.__instancia == None:
            Singleton.__instancia = object.__new__(cls)
            Singleton.__instancia.__Nome = Nome
        
        return Singleton.__instancia
    
    @property
    def Nome(self):
        return self.__Nome
    
    @Nome.setter
    def Nome(self, Nome: str):
        if type(Nome) == str:
            self.__Nome = Nome
            return True
        
        return False
    
if __name__ == "__main__":
    a = Singleton('Teste1')
    print(a.Nome)
    b = Singleton('Teste2')
    print(b.Nome)
    print(a.Nome)