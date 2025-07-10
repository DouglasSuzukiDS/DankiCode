from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html', content=['Flask', 'Python', 'Web Development'])

@app.route('/sobre')
def sobre():
   return '<h2>Sobre</h2>'

@app.route('/noticia/<slug>')
def noticia(slug):
   return f'Noticia: {slug}'