from flask import Flask, jsonify, request,render_template,redirect,url_for
from datetime import *
from main import *
import os.path



app = Flask(__name__)

port='http://127.0.0.1:8000/'

@app.route('/', methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        try:
            pag =  request.form["borrar"]
            usu =  request.form["borrar_usu"]
            
            delect (pag,usu)
            return (render_template("index.html"))
        except:
            print("Not delete method found") 
        try :
            id =  request.form["editar"]
            return (redirect ('http://127.0.0.1:8000/editar/'+id))
        except:
            print("Not edit method found") 
    else:
        if (os.path.isfile('psswords.db') and not os.path.isfile('our_k.key')):
            return render_template("not_key.html")
            
        create_tabla ()
        create_tabla_backup()
        return (render_template("index.html"))
      

@app.route('/password', methods=["GET"])
def get_passwords():
    if ( os.path.isfile('our_k.key')):
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


@app.route('/seach', methods=["POST","GET"])
def list():
    if (request.method == "POST"):
        pag =  request.form["pag"]
        result=buscar_pag(pag)
        rows =result
        return render_template("seach.html",rows = rows)
    else:
         return (render_template("buscador_pag.html"))

@app.route('/editar/<id>', methods=["POST","GET"])
def edit_web(id):
    if (request.method == "POST"):
        pag =  request.form["editar_pag"]
        usu =  request.form["editar_usu"]
        pss =  request.form["editar_pss"]  
       
        editar_(id, pag,pss,usu)

        return redirect ('http://127.0.0.1:8000/')
    else:
         return (render_template("edit.html"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)