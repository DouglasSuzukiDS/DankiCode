# Aula 08 - Args

# O Argumento Arbitratio *args, usado para passar um numero indefinido de parametros, retornando uma tupla

def imprimir_imovel(nomeImovel, n_quartos, vagasGarange=None, *args): 
   print('---------')
   print(f'Titulo: {nomeImovel}')
   print(f'Numero de quartos: {n_quartos}')

   if vagasGarange != None:
      print(f'Vagas na garagem: {vagasGarange}')

imprimir_imovel('Loja Comercial', 2, 5, 'Desconto')

def imprimir_nomes(*nomes):
   print(nomes)
   print(type(nomes))

# imprimir_nomes('Nick', 'Tonhao', 'James')

lista = ['Nick', 'Tonhao', 'James']
imprimir_nomes(lista)