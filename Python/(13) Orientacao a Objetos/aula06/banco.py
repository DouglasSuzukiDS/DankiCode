class Conta:
   # Atributo de Classe
   taxa = 0.50

   # Atributos de Instancia
   def __init__(self, numero, titular, saldo=2000):
      self.numero = numero
      self.titular = titular
      self.saldo = saldo
   
   def extrato(self):
      self.saldo -= Conta.taxa

      print(f'Saldo R$ {self.saldo}')
   
   def depositar(self, valor):
      self.saldo += valor
   
   def sacar(self, valor):
      self.saldo -= valor

# Instancia da Classe Conta
conta1 = Conta(123, 'James')
conta2 = Conta(123, 'Tonhao', 2500)

print(f'Titular: {conta1.titular} - Saldo: R$ {conta1.saldo}')
print(f'Titular: {conta2.titular} - Saldo: R$ {conta2.saldo}')

print(conta1.__dict__) # Exibe os atributos da instância conta1

# Atributo Dinâmico => Criado em tempo de execução
conta2.signo = 'Peixes'
print(conta2.__dict__)