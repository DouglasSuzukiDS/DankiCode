# python -m venv .venv => Cria um ambiente virtual

# python.exe -m pip install --upgrade pip

# ./.venv/Scripts/activate => Ativa o ambiente virtual


''' Caso exista um arquivo requirements.txt, você pode instalar as dependências com o comando abaixo 

# pip install -r requirements.txt

'''

# $env:FLASK_APP = "index" => Seta o arquivo principal da aplicação

''' Caso não contenha um arquivo requirements.txt, você pode instalar o Flask com o comando abaixo '''

# pip install flask => Instala o Flask

# $env:FLASK_APP = "index" => Seta o arquivo principal da aplicação

# $env:FLASK_DEBUG=1 => Garante que o servidor sera reiniciado a cada alteração no código

# $env:FLASK_APP = "development" => Seta o modo de desenvolvimento

# flask run => Inicia o servidor Flask

''' Para gerar o arquivo com as dependências do projeto (seria quase um package.json), você pode usar o comando abaixo: 
   # pip freeze > requirements.txt
'''

# pip install pymysql