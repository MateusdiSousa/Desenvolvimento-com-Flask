from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# criação do app com as funções do flask #
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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
    nome = db.Column(db.String(60))
    descricao = db.Column(db.String(100))
    carga_h = db.Column(db.Integer)

# MÉTODO CONSTRUTOR #
    def __init__(self, nome, descricao, carga_h):
        self.nome = nome
        self.descricao = descricao
        self.carga_h = carga_h
# outras tabelas #
class frutas(db.Model):
    chave2 = db.Column(db.Integer, primary_key = True)
    fruta = db.Column(db.String(20))

    def __init__(self, fruta):
        self.fruta = fruta

class notas(db.Model):
    chave = db.Column(db.Integer, primary_key = True)
    aluno = db.Column(db.String(60), nullable = False)
    nota  = db.Column(db.Integer, nullable = False)

    def __init__(self, aluno, nota):
        self.aluno = aluno
        self.nota = nota

# Delete #
    

# ROTAS #



@app.route('/', methods=['GET', 'POST'])
def main():
    lista_fruta = frutas.query.all()
    if request.method == 'POST':
        fruta = request.form.get('fruta')
        lista = frutas(fruta)
        db.session.add(lista)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('index.html',lista = lista_fruta )

@app.route('/nota', methods = ['GET', 'POST'])
def nota():
    if request.method == 'POST':
        aluno = request.form.get("aluno")
        nota = request.form.get('nota')
        registro = notas(aluno, nota)
        db.session.add(registro)
        db.session.commit()
        return redirect(url_for('nota'))
    return render_template('alunos.html', registros = notas.query.all())

@app.route('/cursos')
def curso():
    return  render_template('cursos.html',cursos = cursos.query.all())

@app.route('/criar_curso', methods = ['GET','POST'])
def add_curso():
    nome = request.form.get('nome')
    desc = request.form.get("descricao")
    ch = request.form.get('carga_h')

    if request.method == 'POST':
            if not nome or not desc or not ch:
                flash("Preencha todos os campos")
            else:
                curso = cursos(nome, desc, ch)
                db.session.add(curso)
                db.session.commit()
                return redirect(url_for('curso'))
    return render_template("addcurso.html")


# Atualizar informações #
@app.route("/<int:chave>/atualiza_curso", methods = ['GET', 'POST'])
def atualiza(chave):
    curso = cursos.query.filter_by(chave = chave).first()
    if request.method == 'POST':
        nome = request.form.get('nome')
        desc = request.form.get('descricao')
        ch = request.form.get('carga_h')

        # Pode ser usando esse método * cursos.query.filter_by(chave = chave).update({'nome':nome,'descricao':desc, 'carga_h':ch})* Ou  Esse:
        curso.nome = nome
        curso.descricao = desc
        curso.carga_h = ch
        db.session.commit()
        return redirect(url_for('curso'))
    return render_template("atualiza_curso.html", curso = curso)

@app.route('/<int:chave>/delete')
def deletar(chave):
    curso = cursos.query.filter_by(chave = chave).first()
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('curso'))


if '__name__' == '__main__':
    app.run(debug = True)
