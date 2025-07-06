# Aula 05 - Objetos
'''
   Paradigma Procedural - Fortran - Sequência, Decisão e a Iteração

   Paradigma Estruturado - C - Structs

   Paradigma Procedural - 
'''

'''# Paradigma Imperativo
from paciente import Registrar

paciente = Registrar('James', 30, '000.000.000-00', 'james@email.com')

print(paciente)'''


# Paradigma Orientado à Objetos
from paciente import Paciente

paciente = Paciente('James', 30, '000.000.000-00', 'james@email.com')

# print(paciente.nome)

'''
   Simulação de Eventos Discretos => Paradigma Orientado à Objetos

   Relação => Destacando funções e variáveis

   --------------------------------------

   Conceitos Estruturais

   - Classe => É uma estrutura que abstrai um conjunto de objetod com caracteristicas similares. Defininfo o comportamento dos seus objetos através das estruturas: 
      1) Aributos
      2) Métodos

   A classe define um tipo de dado abstrato.

   - Abstração => É o processo pelo qual se isolam atributos de um objeto, considerando os que certos grupos de objetos tenham em comum.

   - Reúso => Não existe pior prática em programação do que repetir código.

   - Objeto => Um obbjeto é a representção de um conceito/entidade do mundo real, que pode ser física ou conceitual e possui um significado bem definido para um determinado software.
'''

from banco import Conta

james = Conta(123, 'James', 2000)
james.extrato()
james.depositar(500)
james.extrato()
james.sacar(300)
james.extrato()