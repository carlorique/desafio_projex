from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sqlite3 as sql
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key = "admin123"
app.config['UPLOAD_FOLDER'] = 'static'

@app.route("/")
@app.route("/index")

def index():
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users")
    data=cur.fetchall()
    return render_template ("index.html", datas=data)

@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    if request.method=="POST":
        nome=request.form["nome"]
        tipo=request.form["tipo"]
        captura=request.form["captura"]
        foto=request.form["foto"]
        aparicao=request.form["aparicao"]
        attack=request.form["attack"]
        defesa=request.form["defesa"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("insert into users(NOME,TIPO,CAPTURA,FOTO,APARICAO,ATTACK,DEFESA) values (?,?,?,?,?,?,?)", (nome, tipo, captura, foto, aparicao, attack, defesa))
        con.commit()
        flash("Dados cadastrados com sucesso!", "success")
        return redirect(url_for("index"))
    return render_template("add_user.html")


@app.route("/edit_user/<string:id>", methods=["POST","GET"])
def edit_user(id):
    if request.method=="POST":
        nome=request.form["nome"]
        tipo=request.form["tipo"]
        captura=request.form["captura"]
        foto=request.form["foto"]
        aparicao=request.form["aparicao"]
        attack=request.form["attack"]
        defesa=request.form["defesa"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("update users set NOME=?,TIPO=?,CAPTURA=?,FOTO=?,APARICAO=?,ATTACK=?,DEFESA=? where ID=?", (nome,tipo,captura,foto,aparicao,attack,defesa,id))
        con.commit()
        flash("Dados atualizados com sucesso!", "success")
        return redirect(url_for("index"))
    con=sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where ID =?", (id,))
    data=cur.fetchone()
    return render_template("edit_user.html", datas=data)

@app.route("/delete_user/<string:id>", methods=["GET"])
def delete_user(id):
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("delete from users where ID=?", (id,))
    con.commit()
    flash("Dados deletados com sucesso!", "warning")
    return redirect(url_for("index"))

if __name__=='__main__':
    app.secret_key="admin123"
    app.config['UPLOAD_FOLDER'] = 'static'
    app.run(debug=True)

        




    