from flask import Flask, request, url_for, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
app.config['SECRET_KEY'] = "123"

db = SQLAlchemy(app)

class producto(db.Model):
    id = db.Column("producto_id", db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(100))
    producto_valor = db.Column(db.Integer)
    producto_cantidad = db.Column(db.Integer)
    
    def __init__(self, datos):
        self.producto_nombre = datos["nombre"]
        self.producto_valor = datos["valor"]
        self.producto_cantidad = datos["cantidad"]

@app.route("/")
def principal():
    return render_template("lista.html", productos = producto.query.all())

@app.route("/agregar/<nombre>/<int:valor>/<int:cantidad>")
def agregar(nombre, valor, cantidad):
    datos = {"nombre": nombre, 
             "cantidad": cantidad,
             "valor": valor
    }

    p = producto(datos)
    db.session.add(p)
    db.session.commit()
    data = datos
    data_string = json.dumps(data)
    return redirect(url_for (data_string))
    #return redirect(url_for("principal"))

@app.route("/sacar/<int:id>/<int:cantidad>")
def sacar(id, cantidad):
    p = producto.query.filter_by(id=id).first()
    if cantidad <= p.producto_cantidad:
        p.producto_cantidad = p.producto_cantidad - cantidad
        #data=p.producto_cantidad
        data_string = json.dumps(p.producto_cantidad)
        db.session.commit()
    #data=p.producto_cantidad
    #data_string = json.dumps(data)
    return redirect(url_for (data_string)) #sentencia js
    
    #return redirect(url_for("principal"))


@app.route("/eliminar/<int:id>")
def eliminar(id):
    p = producto.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    data_string = json.dumps(p)
    #return render_template("lista.html", productos = producto.query.all())
    #return redirect(url_for("principal"))
    return redirect(url_for (data_string)) #invocando js

@app.route("/limpiarinventario/")
def limpiarinventario():
    productos=producto.query.all()
    for p in productos:
        db.session.delete(p)
        db.session.commit()
    data_string = json.dumps(productos)
    #return redirect(url_for("principal"))
    return redirect(url_for (data_string)) #invocando js



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)



