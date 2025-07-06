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
      self.__historico = [saldo]
   
   def transacao(self, saldo):
      self.__historico.append(saldo)

   def saldo(self):
      print(f'Saldo R$ {self.__saldo}')
   
   def extrato(self):
      # self.__saldo -= Conta.taxa
      print('--- Extrato Bancário ---')
      print(f'Titular: {self.titular}')

      for saldo in self.__historico:
         print(f'Saldo R$ {saldo}')
   
   def depositar(self, valor):
      self.__saldo += valor
      self.transacao(self.__saldo)
   
   def sacar(self, valor):
      self.__saldo -= valor
      self.transacao(self.__saldo)

   # def transferir(self, valor, origem, destino):
   def transferir(self, valor, destino):
      self.sacar(valor)
      destino.depositar(valor)

# Instancia da Classe Conta
conta1 = Conta(123, 'James')
conta2 = Conta(123, 'Tonhao', 2500)

# print(f'Titular: {conta1.titular} - Saldo: R$ {conta1.extrato()}')
# print(f'Titular: {conta2.titular} - Saldo: R$ {conta2.extrato()}')

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

# conta1.transferir(300, conta1, conta2) # Sem usar a referencia do self
conta1.transferir(300, conta2)
conta1.saldo()
conta2.saldo()
conta1.extrato()