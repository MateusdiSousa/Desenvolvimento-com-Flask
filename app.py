from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# criação do app com as funções do flask #
app = Flask(__name__)

#conexão do banco#
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/teste"

# creação  da extensão da funções do banco #
db = SQLAlchemy(app)

db.init_app(app)

notas = {}
registro = []
lista = [] 

#definção de models #
class cursos(db.Model):
    chave = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(60), unique =True, nullable = False)
    descricao = db.Column(db.String(100))
    carga_h = db.Column(db.Integer, nullable = False)

# MÉTODO CONSTRUTOR #
    def __init__(self, nome, descricao, carga_h):
        self.nome = nome
        self.descricao = descricao
        self.carga_h = carga_h
class frutas(db.Model):
    chave2 = db.Column(db.Integer, primary_key = True)
    fruta = db.Column(db.String(20))

    def __init__(self, fruta):
        self.fruta = fruta

# ROTAS #

@app.route('/', methods=['GET', 'POST'])
def main():
    global lista
    if request.method == 'POST':
        if request.form.get("fruta"):
            lista.append(request.form.get('fruta'))
    return render_template('index.html', lista = lista)

@app.route('/nota', methods = ['GET', 'POST'])
def nota():
    global registro
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get("nota"):
            registro.append({request.form.get('aluno'):request.form.get("nota")})
    return render_template('alunos.html', registro = registro)

@app.route('/cursos')
def curso():
    return  render_template('cursos.html',cursos = cursos.query.all())

@app.route('/criar_curso', methods = ['GET','POST'])
def add_curso():
    nome = request.form.get('nome')
    desc = request.form.get("descricao")
    ch = request.form.get('carga_h')
    if request.method == 'POST':
        curso = cursos(nome, desc, ch)
        db.session.add(curso)
        db.session.commit()
    return render_template("addcurso.html")

if '__name__' == '__main__':
    app.run(debug = True)