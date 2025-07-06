class Pessoa: # Superclasse => Classe mãe
   def __init__(self, nome, data=None, cpf=None, rg=None):
      self.nome = nome
      self.data_nascimento = data
      self.cpf = cpf
      self.rg = rg
      print('Classe Pessoa')
   
   def imprimir_nome(self):
      return self.nome


class Aluno(Pessoa): # Subclasse => Classe filha
   def __init__(self, nome):
      # Pessoa.__init__(self, nome) # Chamada explícita do construtor da superclasse
      super().__init__(nome) # super() chama o construtor da superclasse
      self.matricula = None
      self.notas = []
      print('Classe Aluno')

   def estudar(self):
      return 'Estudando ...'
   
class Professor(Pessoa): # Subclasse => Classe filha
   def __init__(self, nome):
      super().__init__(nome)
      self.disciplinas = []
   
   def lecionar(self):
      return 'Ensinando ...'

aluno1 = Aluno('James')
print(aluno1.imprimir_nome())

professor1 = Professor('Tonhao')
print(professor1.imprimir_nome())

print(type(aluno1))
print(type(professor1))

print(aluno1.estudar())
print(professor1.lecionar())