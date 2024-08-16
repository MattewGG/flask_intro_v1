from flask import Flask, render_template

app = Flask(__name__)
#Isso é feito para que todos os comandos do app possam ser chamados aqui, por issso dar nome pro nosso app.oy
@app.route('/')
def index():
    # return "Ola galera!!!!!" crlt + ; pra comentar tudo 
    #isso exite pra tu poder puxar o lugar e tudo mais
    return render_template('index.html')
@app.route('/variaveis')
def variaveis():
    nome= "Arnaldo Sacomani"
    return render_template('variaveis.html', usuario=nome)

# render_template é massa porque ele permite tu puchar as coisas do html pelo codigo e aplicar as varivais, tipo colocar nome na variavel juja usuario
 
@app.route("/listas")
def listas():
    itens =['item 1', 'item 2', 'item 3', 'item 4']
    return render_template("listas.html", itens=itens)

@app.route("/dicionarios")
def dicionarios():
    usuario_info = {
        "nome": "Gustavo",
        "Idade": 4,
        "Cidade": "jaragua do sul",
        'interesses':["Desenho", "Brincar com blocos", "Jogos de tabuleiro"]
        
    }
    return render_template("dicionarios.html", usuario=usuario_info)

@app.route('/listas_dicionarios')
def listas_dcicionarios():
    usuarios = [
        {'nome': "Gustavo", 'idade': 4, "cidade": "Jaragua do sul"},
        {'nome': "Aravos", 'idade': 2, "cidade": "Guaramirim"}
    ]
        
    return render_template('listas_dicionarios.html', usuarios=usuarios)
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    