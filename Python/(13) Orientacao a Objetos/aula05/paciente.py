# Paradigma Imperativo
def Registrar(nome, idade, cpf, email):
   paciente = { 'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email }

   return paciente

# Paradigma Orientado à Objetos
''' 
   Classe => Um conjunto de objetoscom as mesmas caracteristicas
   Objeto => Representalçao do mundo real como um tipo de dado de uma classe 
   Construtor => É a função criada implicitamente com o omesmo nome da classe
   Atributo => São as variáveis de uima classe
'''

class Paciente:
   def __init__(self, nome, idade, cpf, email):
      self.nome = nome
      self.idade = idade
      self.cpf = cpf
      self.email = email