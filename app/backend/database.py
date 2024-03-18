import flask_sqlalchemy as sa
import pandas as pd

db = sa.SQLAlchemy()

def init_db(db, filename=None):
    if filename:
        df = pd.read_csv(filename)
        df.to_sql('inventory', con=db.engine, if_exists='replace', index=False)
    db.create_all()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    conferma = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f"Order('{self.nome}', '{self.timestamp}', '{self.conferma}')"

class Inventory(db.Model):
    nome = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    macrocategoria = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    sottocategoria = db.Column(db.String(100), nullable=False)
    materiali = db.Column(db.String(100), nullable=False)
    peso = db.Column(db.Float, nullable=False)
    prezzo = db.Column(db.Float, nullable=False)
    dimensioni = db.Column(db.String(100), nullable=False)
    colore = db.Column(db.String(100), nullable=False)
    disegno = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    features = db.Column(db.String(100), nullable=False)
    descrizione_intorto = db.Column(db.String(100), nullable=False)
    descrizione_tecnica = db.Column(db.String(100), nullable=False)
    variante1 = db.Column(db.String(100), nullable=False)
    variante2 = db.Column(db.String(100), nullable=False)
    variante3 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Inventory('{self.nome}', '{self.macrocategoria}', '{self.categoria}')"