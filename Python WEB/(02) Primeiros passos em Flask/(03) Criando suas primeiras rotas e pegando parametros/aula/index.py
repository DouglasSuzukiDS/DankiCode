from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return '<h2>Hello World!</h2>'

@app.route('/sobre')
def sobre():
   return '<h2>Sobre</h2>'

@app.route('/noticia/<slug>')
def noticia(slug):
   return f'Noticia: {slug}'