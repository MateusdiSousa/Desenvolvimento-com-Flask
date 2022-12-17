from flask import Flask, render_template, request

app = Flask(__name__)
notas = {}
registro = []
lista = [] 
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

if '__name__' == ('__main__'):
    app.run(debug = True)