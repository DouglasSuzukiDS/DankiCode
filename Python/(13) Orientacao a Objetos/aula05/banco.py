class Conta:
   def __init__(self, numero, titular, saldo):
      self.numero = numero
      self.titular = titular
      self.saldo = saldo
   
   def extrato(self):
      print(f'Saldo R$ {self.saldo}')
   
   def depositar(self, valor):
      self.saldo += valor
   
   def sacar(self, valor):
      self.saldo -= valor