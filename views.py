#Possibilité de mettre nos routes dans le app.py après initialisation de l'app, mais ici on les orgnasiera sous forme de Blueprint
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, send_file

#Initialisation du Blueprint
views = Blueprint(__name__, "views")

@views.route("/") 
def home():
    #Retourner un code html
    return render_template('index.html', name="Cyriac", age= 20) #on peut ajouter autant de variables que l'on veut et y acceder dans index.html avec {{variable}}

@views.route("/projects")
def profile():
    return render_template('projects.html')

@views.route("/json")
def get_json():
    #Ici, on jsonify un dico python
    return jsonify({'name' : 'cyriac', 'coolness' : 40, 'r' : 0})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/file-downloads")
def file_downloads():
    try:
        return render_template("downloads.html")
    except Exception as e:
        return str(e)
    
@views.route("/return-files")
def return_files():
    try:
        return send_file("static/files/cyriac-thibaudeau.pdf", as_attachment="cvcyriac.pdf")
    except Exception as e:
        return str(e)
    
@views.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("views.user", usr=user))
    else:
        return render_template("login.html")

@views.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@views.route("/test2")
def test():
    return render_template("test2.html")