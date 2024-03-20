import os
from flask import Flask, request, jsonify
from flask_cors import cross_origin
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
@cross_origin()
def get():
    nome = request.args.get('nome')
    if nome:
        item = Inventory.query.filter_by(nome=nome).first_or_404()
        result = {"categoria": item.categoria, "sottocategoria": item.sottocategoria, "nome": item.nome, "materiali": item.materiali, "peso": item.peso, "prezzo": item.prezzo, "dimensioni": item.dimensioni, "foto": item.foto, "link": item.link}
        response = jsonify(result)
        return response
    else:
        inventory = Inventory.query.order_by(Inventory.categoria, Inventory.sottocategoria, Inventory.nome).all()
        result = [{"categoria": item.categoria, "sottocategoria": item.sottocategoria, "nome": item.nome, "materiali": item.materiali, "peso": item.peso, "prezzo": item.prezzo, "dimensioni": item.dimensioni, "foto": item.foto, "link": item.link} for item in inventory]
        response = jsonify(result)
        return response

@app.get("/headers")
@cross_origin()
def headers():
    categorie = Inventory.query.with_entities(Inventory.categoria).distinct().all()
    categorie = [i[0] for i in categorie]
    categorie.sort()
    sottocategorie = Inventory.query.with_entities(Inventory.sottocategoria).distinct().all()
    sottocategorie = [i[0] for i in sottocategorie]
    sottocategorie.sort()
    headers = [{"name": "categoria", "type": "select", "selectOptions": categorie},
                {"name": "sottocategoria", "type": "select", "selectOptions": sottocategorie},
                {"name": "nome", "type": "text"},
                {"name": "materiali", "type": "text"},
                {"name": "peso", "type": "number"},
                {"name": "prezzo", "type": "number"},
                {"name": "dimensioni", "type": "text"},
                {"name": "foto", "type": "text"},
                {"name": "link", "type": "text"}
               ]
    response = jsonify(headers)
    return response

@app.get("/getCategorie")
@cross_origin()
def getCategorie():
    categorie = Inventory.query.with_entities(Inventory.categoria).distinct().all()
    result = [i[0] for i in categorie]
    result.sort()
    response = jsonify(result)
    return response

@app.get("/getSottocategorie")
@cross_origin()
def getSottocategorie():
    sottocategorie = Inventory.query.with_entities(Inventory.sottocategoria).distinct().all()
    result = [i[0] for i in sottocategorie]
    result.sort()
    response = jsonify(result)
    return response

@app.post('/add')
@cross_origin()
def add():
    for i in ["categoria", "sottocategoria", "nome", "materiali", "peso", "prezzo", "dimensioni", "foto", "link"]:
        if i not in request.form:
            response = jsonify(f"Missing parameter {i}")
            return response
    categoria = request.form.get('categoria')
    sottocategoria = request.form.get('sottocategoria')
    nome = request.form.get('nome')
    materiali = request.form.get('materiali')
    peso = request.form.get('peso')
    prezzo = request.form.get('prezzo')
    dimensioni = request.form.get('dimensioni')
    foto = request.form.get('foto')
    link = request.form.get('link')
    item = Inventory(categoria=categoria, sottocategoria=sottocategoria, nome=nome, materiali=materiali, peso=peso, prezzo=prezzo, dimensioni=dimensioni, foto=foto, link=link)
    db.session.add(item)
    db.session.commit()
    response = jsonify("Item added")
    return response

@app.get("/remove")
@cross_origin()
def remove():
    nome = request.args.get('nome')
    if nome:
        item = Inventory.query.filter_by(nome=nome).first_or_404()
        db.session.delete(item)
        db.session.commit()
        response = jsonify("Item removed")
        return response
    else:
        response = jsonify("Missing parameters")
        return response

@app.get("/sell")
@cross_origin()
def sell():
    nome = request.args.get('nome')
    if nome:
        Inventory.query.filter_by(nome=nome).first_or_404()
        order = Order(nome=nome)
        db.session.add(order)
        db.session.commit()
        response = jsonify("Item awaiting confirmation")
        response.status_code = 200
        return response
    else:
        response = jsonify("Missing parameters")
        response.status_code = 200
        return response

@app.get("/control")
@cross_origin()
def control_get():
    orders = Order.query.all()
    result = [{"id": i.id, "nome": i.nome, "timestamp": i.timestamp, "conferma": i.conferma} for i in orders]
    response = jsonify(result)
    response.status_code = 200
    return response

@app.post("/control")
@cross_origin()
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
        response = jsonify("Done")
        return response
    else:
        response = jsonify("Missing parameters")
        return response

app.run(debug=False)