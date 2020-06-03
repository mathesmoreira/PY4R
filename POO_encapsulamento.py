#MODIFICADORES DE ACESSO E MÉTODOS DE CLASSE

class Conta:
    #Atributo de classe
    _total_contas = 0 

    def __init__(self, numero, titular, saldo = 0.0, limite = 1000.0):
        # Atributos de instância
        self.numero = numero
        self.tutular = titular
        ## Atributo privado
        self.__saldo = saldo                
        self.limite = limite
        Conta._total_contas += 1

    # MÉTODOS ESTÁTICOS
    # Métodos estáticos não precisam de uma referência, não recebem um primeiro argumento especial (self)
    @staticmethod
    def get_total_contas():
        # Como 'total_contas' é uma var. classe devemos chama-la pela classe
        return Conta._total_contas   
    
    def saca(self,valor):
        self.__saldo -= valor

    #ENCAPSULAMENTO
    # Usando um decorador para trabalhar com os métodos get e set, ambos retorna o valor do attr privado
    @property 
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print('Saldo não pode ser negativo')
        else:
            self.__saldo = saldo


minha_conta = Conta('123-4', 'joão', 1000.0, 2000.0)
print(minha_conta.saldo)
#Através dos decoradores, Property e .setter, podemos chamar os métodos como atributos públicos
#minha_conta.saldo = -100.0
c1 = Conta('123-5','Josefino', 2000.0)
print(Conta.get_total_contas())

# #Acessando um atributo privado
# minha_conta._Conta__saldo
# #Mostrando que o atributo saldo foi renomeado na classe Conta para _Conta__saldo
# print(dir(minha_conta))
# #Caso tente modifica-lo, irá surgir um novo atributo dentro da classe
# minha_conta.__saldo = 2000
# print(dir(minha_conta))

