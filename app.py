from flask import Flask, render_template, request

app = Flask(__name__)
notas = {'Mariana':10, 'Sérgio':5, 'Mateus':9, 'Cláudia':10}
lista = [] 
@app.route('/', methods=['GET', 'POST'])
def main():
    global lista
    if request.method == 'POST':
        if request.form.get("fruta"):
            lista.append(request.form.get('fruta'))
    return render_template('index.html', lista = lista)

@app.route('/nota')
def nota():
    return render_template('alunos.html', notas = notas)

if '__name__' == ('__main__'):
    app.run(debug = True)