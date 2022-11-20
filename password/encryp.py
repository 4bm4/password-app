from datetime import *
from cryptography.fernet import Fernet
import os.path 


def generat_key ():
    if(not os.path.isfile("our_k.key")):
        key=Fernet.generate_key()
        with open("our_k.key","wb") as file:
            file.write(key)


def load_key():
    return open("our_k.key","rb").read()


def cryp_file(bol:bool,data:str,key):
    
    try:
        f=Fernet (key)
        encryp_dta=f.encrypt(data)
        return (encryp_dta)
    except Exception:
        print("The file couldn't be encrypted")
    

def decryp(bol:bool,data,key): 
    try:
        key=load_key()
        f=Fernet (key)
        decryp_dta=f.decrypt(data)
        return (decryp_dta)

    except Exception:
        print(f"\nProblem reading: {data} -----> the document could not be encrypted\n")
    


def all_cryp (clase):
    if (not clase.act):
        try:
            generat_key()
            key=load_key()

            pss_enc=cryp_file(clase.act,clase.password[0].encode('utf-8'),key)
            clase.password[0]=pss_enc.decode("utf-8")

            usu_enc=cryp_file(clase.act,clase.usu.encode('utf-8'),key)
            clase.usu=usu_enc.decode("utf-8")

            pag_enc=cryp_file(clase.act,clase.pag.encode('utf-8'),key)
            clase.pag=pag_enc.decode("utf-8")

            clase.act=True
            clase.ultima=clase.ultima
            return (clase)

        except Exception:
            print(f"\nProblem reading: {clase.password[0]} -----> the document could be already encrypted\n")
    else:
        print("ya estaba encriptado")    

def all_decryp (clase):
    if (clase.act):
        try:
            generat_key()
            key=load_key()

            pss_enc=decryp(clase.act,clase.password[0].encode('utf-8'),key)
            clase.password[0]=pss_enc.decode("utf-8")

            usu_enc=decryp(clase.act,clase.usu.encode('utf-8'),key)
            clase.usu=usu_enc.decode("utf-8")

            pag_enc=decryp(clase.act,clase.pag.encode('utf-8'),key)
            clase.pag=pag_enc.decode("utf-8")

            clase.act=False
            clase.ultima=clase.ultima
            return (clase)

        except Exception:
            print(f"\nProblem reading: {clase.password[0]} -----> the document could be already encrypted\n")
    else:
        print("ya estaba desencriptado")   



