
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp.db'
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    preco = db.Column(db.Float)

@app.route('/')
def home():
    return {'sistema': 'Mini ERP'}

@app.route('/produtos', methods=['GET','POST'])
def produtos():
    if request.method == 'POST':
        d = request.json
        p = Produto(nome=d['nome'], preco=d['preco'])
        db.session.add(p)
        db.session.commit()
        return {'status':'criado'}
    return jsonify([{'id':p.id,'nome':p.nome,'preco':p.preco} for p in Produto.query.all()])

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
