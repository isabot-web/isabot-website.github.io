from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para a categoria de comandos normais
@app.route("/normais")
def normais():
    return render_template("normais.html")

# Rota para a categoria de comandos de administração
@app.route("/adm")
def adm():
    return render_template("adm.html")

# Rota para a categoria de comandos de entretenimento
@app.route("/entretenimento")
def entretenimento():
    return render_template("entretenimento.html")

if __name__ == "__main__":
    app.run(debug=True)
