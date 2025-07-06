class Conta:
   # Privated => Uso de __
   # Protected => Uso de _

   # Atributo de Classe
   taxa = 0.50

   @classmethod
   def retornarCodigo(cls):
      print('Codigo: 555')

   @staticmethod
   def retornarCodigoBanco():
      return '345'

   # Atributos de Instancia 
   def __init__(self, numero, titular, saldo=2000):
      self._numero = numero # Visibilidade Protegida (Protected)
      self.titular = titular # Visibilidade Pública (Public)
      self.__saldo = saldo # Visibilidade Privada (Private)
   
   def extrato(self):
      self.__saldo -= Conta.taxa

      print(f'Saldo R$ {self.__saldo}')
   
   def depositar(self, valor):
      self.__saldo += valor
   
   def sacar(self, valor):
      self.__saldo -= valor

# Instancia da Classe Conta
conta1 = Conta(123, 'James')
conta2 = Conta(123, 'Tonhao', 2500)

print(f'Titular: {conta1.titular} - Saldo: R$ {conta1.extrato()}')
print(f'Titular: {conta2.titular} - Saldo: R$ {conta2.extrato()}')

print(conta1.__dict__) # Exibe os atributos da instância conta1

# Atributo Dinâmico => Criado em tempo de execução
conta2.signo = 'Peixes'
print(conta2.__dict__)

# Método da Clasee
Conta.retornarCodigo() # Convenção
conta1.retornarCodigo()

# Método Estático
print(Conta.retornarCodigoBanco()) # Convenção
print(conta1.retornarCodigoBanco())