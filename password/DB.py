import sqlite3
import os.path 


def create_tabla():
    if(not os.path.isfile("psswords.db")):
        db=sqlite3.connect('psswords.db')
        manejo_db=db.cursor()
        manejo_db.execute(""" CREATE TABLE IF NOT EXISTS psswords (
        id text,
        usuario text,
        pagina text,
        password text,
        fecha text,
        act integer,
        ultima integer)""")
        db.commit()
        db.close()
    
def create_tabla_backup():
    if(not os.path.isfile("psswords_backup.db")):
        db=sqlite3.connect('psswords_backup.db')
        manejo_db=db.cursor()
        manejo_db.execute(""" CREATE TABLE IF NOT EXISTS psswords (
        id text,
        usuario text,
        pagina text,
        password text,
        fecha text,
        act integer,
        ultima integer)""")
        db.commit()
        db.close()

def insert_element(DB:str,elemento):
    db=sqlite3.connect(DB)
    manejo_db=db.cursor()
    if (elemento.act==True):
        elemento_aux=1
    else:
        elemento_aux=0
    if (elemento.ultima==True):
        elemento_aux2=1
    else:
        elemento_aux2=0
    manejo_db.execute("INSERT INTO psswords VALUES (?,?,?,?,?,?,?)", (elemento.id,elemento.usu, elemento.pag, elemento.password[0],elemento.fecha,elemento_aux,elemento_aux2))
    db.commit()
    db.close()



def select_element(id):
    
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    manejo_db.execute("SELECT * FROM psswords WHERE id=?",(id,))
    elemento=manejo_db.fetchone()
    db.close()
    return elemento

def select_element_pag(pag):
    
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    manejo_db.execute("SELECT * FROM psswords WHERE pagina=?",(pag,))
    elemento=manejo_db.fetchone()
    db.close()
    return elemento    

def select_element_all():
    
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    manejo_db.execute("SELECT * FROM psswords ")
    elemento=manejo_db.fetchall()
    db.close()
    return elemento    



def select_varios_pag(pag):
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    manejo_db.execute("SELECT * FROM psswords WHERE pagina=?",(pag,))
    elemento=manejo_db.fetchall()
    db.close()
    return elemento    

#editar usuario
def update_element_usu(id,elemeto_a_act):
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    manejo_db.execute("UPDATE psswords SET usuario=? WHERE id=?",(elemeto_a_act,id))
    db.commit()
    db.close()

#editar password
def update_element_pss(id,elemeto_a_act):
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    manejo_db.execute("UPDATE psswords SET password=? WHERE id=?",(elemeto_a_act,id))
    db.commit()
    db.close()

#editar pag
def update_element_pss(id,elemeto_a_act):
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    manejo_db.execute("UPDATE psswords SET pagina=? WHERE id=?",(elemeto_a_act,id))
    db.commit()
    db.close()

def update_element_ultima(id,elemeto_a_act):
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    if (elemeto_a_act):
        elemento_aux2=1
    else:
        elemento_aux2=0
    manejo_db.execute("UPDATE psswords SET ultima=? WHERE id=?",(elemento_aux2,id))
    db.commit()
    db.close()
   
    
def delect_element(id):
    db=sqlite3.connect('psswords.db')
    manejo_db= db.cursor()
    manejo_db.execute("DELETE FROM psswords WHERE id=?",(id,))
    db.commit()
    db.close()

def sacar_pags():
    if( os.path.isfile("our_k.key")):
        db=sqlite3.connect('psswords.db')
        manejo_db= db.cursor()
        manejo_db.execute("SELECT pagina FROM psswords ")
        elemento=manejo_db.fetchall()
        db.close()

        if (isinstance(elemento,tuple)):

            return(elemento[0])

        elif (isinstance(elemento,list)):
            clase=[]

            for i in elemento:
                clase.append( i[0])

        return clase    


