import os
from flask import Flask, request, jsonify
from database import Inventory, Order, init_db, db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    #init_db(db, os.path.join(basedir,'database.csv')) # Rimuovere il secondo parametro una volta creato il database
    init_db(db)

@app.get("/get")
def get():
    nome = request.args.get('nome')
    if nome:
        item = Inventory.query.filter_by(nome=nome).first_or_404()
        result = {"nome": item.nome, "macrocategoria": item.macrocategoria, "categoria": item.categoria, "sottocategoria": item.sottocategoria, "materiali": item.materiali, "peso": item.peso, "prezzo": item.prezzo, "dimensioni": item.dimensioni, "colore": item.colore, "disegno": item.disegno, "foto": item.foto, "link": item.link, "features": item.features, "descrizione_intorto": item.descrizione_intorto, "descrizione_tecnica": item.descrizione_tecnica, "variante1": item.variante1, "variante2": item.variante2, "variante3": item.variante3}
        return jsonify(result)
    else:
        inventory = Inventory.query.all()
        result = [{"nome": i.nome, "macrocategoria": i.macrocategoria, "categoria": i.categoria, "sottocategoria": i.sottocategoria, "materiali": i.materiali, "peso": i.peso, "prezzo": i.prezzo, "dimensioni": i.dimensioni, "colore": i.colore, "disegno": i.disegno, "foto": i.foto, "link": i.link, "features": i.features, "descrizione_intorto": i.descrizione_intorto, "descrizione_tecnica": i.descrizione_tecnica, "variante1": i.variante1, "variante2": i.variante2, "variante3": i.variante3} for i in inventory]
        return jsonify(result)

@app.post("/add")
def add():
    nome = request.form.get('nome')
    macrocategoria = request.form.get('macrocategoria')
    categoria = request.form.get('categoria')
    sottocategoria = request.form.get('sottocategoria')
    materiali = request.form.get('materiali')
    peso = request.form.get('peso')
    prezzo = request.form.get('prezzo')
    dimensioni = request.form.get('dimensioni')
    colore = request.form.get('colore')
    disegno = request.form.get('disegno')
    foto = request.form.get('foto')
    link = request.form.get('link')
    features = request.form.get('features')
    descrizione_intorto = request.form.get('descrizione_intorto')
    descrizione_tecnica = request.form.get('descrizione_tecnica')
    variante1 = request.form.get('variante1')
    variante2 = request.form.get('variante2')
    variante3 = request.form.get('variante3')
    if not nome or not macrocategoria or not categoria or not sottocategoria or not materiali or not peso or not prezzo or not dimensioni or not colore or not disegno or not foto or not link or not features or not descrizione_intorto or not descrizione_tecnica or not variante1 or not variante2 or not variante3:
        return jsonify("Missing parameters")
    item = Inventory(nome=nome, macrocategoria=macrocategoria, categoria=categoria, sottocategoria=sottocategoria, materiali=materiali, peso=peso, prezzo=prezzo, dimensioni=dimensioni, colore=colore, disegno=disegno, foto=foto, link=link, features=features, descrizione_intorto=descrizione_intorto, descrizione_tecnica=descrizione_tecnica, variante1=variante1, variante2=variante2, variante3=variante3)
    db.session.add(item)
    db.session.commit()
    return jsonify("Item added")

@app.get("/remove")
def remove():
    nome = request.args.get('nome')
    if nome:
        item = Inventory.query.filter_by(nome=nome).first_or_404()
        db.session.delete(item)
        db.session.commit()
        return jsonify("Item removed")
    else:
        return jsonify("Missing parameters")

@app.get("/sell")
def sell():
    nome = request.args.get('nome')
    if nome:
        Inventory.query.filter_by(nome=nome).first_or_404()
        order = Order(nome=nome)
        db.session.add(order)
        db.session.commit()
        return jsonify("Item awaiting confirmation")
    else:
        return jsonify("Missing parameters")

@app.get("/control")
def control_get():
    orders = Order.query.all()
    result = [{"id": i.id, "nome": i.nome, "timestamp": i.timestamp, "conferma": i.conferma} for i in orders]
    return jsonify(result)

@app.post("/control")
def control_post():
    id = request.form.get('id')
    conferma = request.form.get('conferma')
    if id and conferma:
        conferma = True if conferma == "True" else False
        order = Order.query.filter_by(id=id).first_or_404()
        order.conferma = conferma
        item = Inventory.query.filter_by(nome=order.nome).first_or_404() # già venduto
        if conferma:
            db.session.delete(item)
        db.session.commit()
        return jsonify("Done")
    else:
        return jsonify("Missing parameters")

app.run(debug=False)