class Aluno:
   def __init__(self, nome, idade, matricula):
      self.__nome = nome
      self._idade = idade
      self.matricula = matricula
      self.notas = None
   
   '''def get_nome(self):
      return self.__nome'''
   
   @property
   def nome(self):
      return self.__nome
   
   '''def set_nome(self, nome):
      self.__nome = nome
   '''

   @nome.setter
   def nome(self, nome):
      self.__nome = nome

   '''def get_idade(self):
      return self._idade'''
   
   @property
   def idade(self):
      return self._idade
   
   ''' def set_idade(self, idade):
      self._idade = idade '''
     
   @idade.setter
   def idade(self, idade):
      self._idade = idade

aluno1 = Aluno('Jose', 15, 123456)
print(aluno1.nome)
aluno1.nome = 'Joseph'
print(aluno1.nome)


print(aluno1.idade)
aluno1.idade = 16
print(aluno1.idade)

print(aluno1.matricula)
print(aluno1.notas)