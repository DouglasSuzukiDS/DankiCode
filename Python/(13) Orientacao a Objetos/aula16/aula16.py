# Aula 16 - Herança Multipla

class Funcionario:
   def trabalhar(self):
      print('Trabalhando ...')

class Frontend(Funcionario):
   def trabalhar(self):
      print('Frontend ...')
   
   def front_end(self):
      super().trabalhar()

class Backend(Funcionario):
   def trabalhar(self):
      print('Backend ...')

   def back_end(self):
      super().trabalhar()

class Fullstack(Frontend, Backend):
   pass

jose = Frontend()
marcos = Backend()
ana = Fullstack()

jose.trabalhar()
marcos.trabalhar()
ana.trabalhar()
ana.front_end
ana.back_end()