from flask import Flask, render_template, request, session, make_response
import pymysql

# Imports necessarios para puxar dados dos arquivo .env
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = 'rojmbgoriÇre56ç48g'

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

# Necessario criar o DB flask com a table CLIENTES no MySQL antes de rodar o app
db = pymysql.connect(host='localhost', user=user, password=password, db='flask')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
   if request.method == 'GET':
      # return render_template('index.html', content=['Flask', 'Python', 'Web Development'])

      '''if 'usuario' in session:
         usuario = session['usuario']
      else:
         session['usuario'] = 'Nick'

      return session['usuario']'''

      if request.cookies.get('usuario'):
         resp = make_response('Meu site com Cookie')
         resp.set_cookie('usuario', 'Nick')
      else:
         resp = make_response('Meu site sem Cookie')
         resp.set_cookie('usuario', 'Nick')

      cursor = db.cursor()
      sql = 'SELECT * FROM clientes'
      cursor.execute(sql)
      results = cursor.fetchall()
      print(results)
      
      return render_template('index.html', content=results)

   else:
      return f'Enviado do form: {request.form['conteudo']}'

@app.route('/sobre')
def sobre():
   return '<h2>Sobre</h2>'

@app.route('/noticia/<slug>')
def noticia(slug):
   return f'Noticia: {slug}'