from flask import Flask, render_template, request, session, make_response, redirect
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
def index():
   if request.method == 'POST':
      id = request.form.get('id')
      nome = request.form['nome']
      email = request.form['email']

      cursor = db.cursor()
      sql = 'UPDATE clientes SET name = %s, email = %s WHERE id = %s'
      cursor.execute(sql, (nome, email, id))
      db.commit()

      cursor = db.cursor()
      sql = 'SELECT * FROM clientes'
      cursor.execute(sql)
      db.commit()
      results = cursor.fetchall()
      print(results)

      return render_template('index.html', content=results)
   else:
      cursor = db.cursor()
      sql = 'SELECT * FROM clientes'
      cursor.execute(sql)
      db.commit()
      results = cursor.fetchall()
      print(results)

      return render_template('index.html', content=results)

@app.route('/deletar', methods=['GET', 'POST'])
def deletar():
   # request.args.get('id') => Retorna o ID
   cursor = db.cursor()
   sql = 'DELETE FROM clientes WHERE id = %s'
   cursor.execute(sql, (request.args.get('id'),))
   db.commit()

   return redirect('/')

@app.route('/sobre')
def sobre():
   return '<h2>Sobre</h2>'

@app.route('/noticia/<slug>')
def noticia(slug):
   return f'Noticia: {slug}'