from datetime import date

class Paciente:
   def __init__(self, nome, idade, cpf, email):
      self.nome = nome
      self.idade = idade
      self.cpf = cpf
      self.email = email

   '''@classmethod
   def idadeAnoNascimento(cls, anosNascimento):
      return (date.today().year - anosNascimento)'''
   
   @classmethod
   def idadeAnoNascimento(cls, nome, anoNascimento, cpf, email):
      idade = date.today().year - anoNascimento
      return cls(nome, idade, cpf, email)

class Medico:
   pass

'''paciente = Paciente('James', 30, '000.000.000-00', 'james@email.com')
print(paciente.__dict__)
print(Paciente.idadeAnoNascimento(2001))'''

paciente = Paciente.idadeAnoNascimento('James', 1957, '000.000.000-00', 'james@email.com')
print(paciente.__dict__)
print(paciente.idade)