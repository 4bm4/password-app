from flask import Flask, jsonify, request,render_template,redirect,url_for
from datetime import *
from main import *


app = Flask(__name__)

# Your port
port='http://127.0.0.1:8000/'

@app.route('/', methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        pag =  request.form["borrar"]
        print(pag)
        delect (pag)
        return (render_template("index.html"))
    else:
        create_tabla ()
        return (render_template("index.html"))
      

@app.route('/password', methods=["GET"])
def get_passwords():
    Passwords = buscar_todas()
    return jsonify(Passwords)


@app.route("/password/incluir", methods=["POST", "GET"])
def insert_passwords():
    if (request.method == "POST"):
    
        usur =  request.form["usu"]
        pag =  request.form["pag"]
        clase=pss(
            pag=pag,
            fecha=datetime.now().strftime('%Y-%m-%d'),
            usu=usur,
            password=[pwd_generator()]
            )
        introducir_clase (clase)
        
        return (redirect (port))
    
        
    else:
        return (render_template("contrasenias_enternew.html"))


@app.route("/actualizar",methods=["POST", "GET"])
def update_passwords():
    render_template("index.html")
    actualizar()
    return render_template("index.html")
    

@app.route("/password/buscar", methods=["POST","GET"])
def buscar():
    if (request.method == "POST"):
        pag =  request.form["pag"]
        return  redirect (url_for(f'password/buscar/{pag}'))
    else:
         return (render_template("buscador_pag.html"))


@app.route('/list', methods=["POST","GET"])
def list():
    if (request.method == "POST"):
        pag =  request.form["pag"]
        result=buscar_pag(pag)
        rows =result
        return render_template("list.html",rows = rows)
    else:
         return (render_template("buscador_pag.html"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)