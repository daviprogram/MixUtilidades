from flask import Flask, render_template

app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    produtos = [
        {"nome": "Arroz", "preco": "R$ 25,00", "imagem": "arroz.jpeg"},
        {"nome": "Feijão", "preco": "R$ 7,50", "imagem": "feijao.jpeg"},
        {"nome": "Óleo", "preco": "R$ 6,99", "imagem": "oleo.jpeg"},
        {"nome": "Macarrão", "preco": "R$ 3,90", "imagem": "macarrao.jpeg"}
    ]
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
