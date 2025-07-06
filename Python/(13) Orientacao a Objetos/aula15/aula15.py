# Aula 15 - Classes Abstratas

from abc import ABC, abstractmethod

# Classe Abstrata
class Pessoa(ABC): # Superclasse => Classe mãe
   def __init__(self, nome=None, data=None, cpf=None, rg=None):
      self.nome = nome
      self.data_nascimento = data
      self.cpf = cpf
      self.rg = rg
      print('Classe Pessoa')

   def imprimir_nome(self):
      return self.nome

   @abstractmethod
   def trabalhar(self): 
      print('Implemente a funcionalidade do método')

# Classe Concreta
class Administrador(Pessoa):
   def trabalhar(self):
      return super().trabalhar() # Chamada do método abstrato da superclasse

# Classe Concreta 
class Professor(Pessoa): # Subclasse => Classe filha
   def __init__(self, nome):
      super().__init__(nome)
      self.disciplinas = []
   
   def trabalhar(self):
      nome_classe = self.__class__.__name__  
      print(f'Classe {nome_classe} Ensinando ...')

# Classe Concreta
class Aluno(): # Subclasse => Classe filha
   def __init__(self, nome):
      # Pessoa.__init__(self, nome) # Chamada explícita do construtor da superclasse
      super().__init__(nome) # super() chama o construtor da superclasse
      self.matricula = None
      self.notas = []
      print('Classe Aluno')

   def estudar(self):
      print('Estudando ...')

profesor1 = Professor('James')
administrador = Administrador()
administrador.trabalhar()
profesor1.trabalhar()