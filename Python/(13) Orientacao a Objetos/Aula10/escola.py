class Quadrado:
   def __init__(self, lado):
      self.__lado = lado
      self.__area = lado * lado

   def retorna_area(self):
      print(f'Área do quadrado: {self.__area}')

quadrado = Quadrado(2)
quadrado.retorna_area()
quadrado.__area = 7
quadrado.retorna_area()
print(quadrado.__dict__)

# Name Mangling _Classe_atributo