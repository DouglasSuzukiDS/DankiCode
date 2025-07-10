from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
   if request.method == 'GET':
      return render_template('index.html', content=['Flask', 'Python', 'Web Development'])
   else:
      return f'Enviado do form: {request.form['conteudo']}'

@app.route('/sobre')
def sobre():
   return '<h2>Sobre</h2>'

@app.route('/noticia/<slug>')
def noticia(slug):
   return f'Noticia: {slug}'