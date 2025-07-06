# Aula 14 - Polimorfismo

class Pessoa: # Superclasse => Classe mãe
   def __init__(self, nome=None, data=None, cpf=None, rg=None):
      self.nome = nome
      self.data_nascimento = data
      self.cpf = cpf
      self.rg = rg

   def imprimir_nome(self):
      return self.nome

   def trabalhar(self): 
      pass

class Administrador(Pessoa):
   def trabalhar(self):
      nome_classe = self.__class__.__name__  
      print(f'Classe {nome_classe} Organizando planilhas ...')
   
class Professor(Pessoa): # Subclasse => Classe filha
   def __init__(self, nome):
      super().__init__(nome)
      self.disciplinas = []
   
   def trabalhar(self):
      nome_classe = self.__class__.__name__  
      print(f'Classe {nome_classe} Ensinando ...')

class Aluno(Pessoa): # Subclasse => Classe filha
   def __init__(self, nome):
      # Pessoa.__init__(self, nome) # Chamada explícita do construtor da superclasse
      super().__init__(nome) # super() chama o construtor da superclasse
      self.matricula = None
      self.notas = []
      print('Classe Aluno')

   def estudar(self):
      print('Estudando ...')

professor1 = Professor('James')
administrador1 = Administrador()

professor1.trabalhar()
administrador1.trabalhar()