from password.encryp import all_cryp, all_decryp
from password.funtion_pss import *
from password.clas import *
from password.DB import *

def introducir_clase(clase):
    create_tabla()
    paginas_ant=buscar_pag(clase.pag)
    if (paginas_ant):
        for i in paginas_ant:
            i.ultima=False
            update_element_ultima(i.id,i.ultima)
    clase_encrip = all_cryp(clase)
    insert_element(clase_encrip)


def buscar_pag(pag: str):
    todas_encrip = select_element_all()
    aux = transf_arr_clase(todas_encrip)
    lista_desencript = []
    resultado = []
    for i in aux:
        lista_desencript.append(all_decryp(i))

    for i in lista_desencript:
        if (i.pag == pag):
            resultado.append(i)

    return (resultado)


def buscar_todas():
    todas_encrip = select_element_all()
    aux = transf_arr_clase(todas_encrip)
    lista_desencript = []
    resultado = []
    for i in aux:
        lista_desencript.append(all_decryp(i))

    for i in lista_desencript:
        if (i.ultima):
            resultado.append(i)
            
    return (resultado)


def actualizar():
    elementos = buscar_todas()
    now = datetime.now().strftime('%Y-%m-%d')
    today = datetime.strptime(now, '%Y-%m-%d')
    for i in elementos:
        dif_days = today-datetime.strptime(i.fecha, '%Y-%m-%d')
        if (dif_days > timedelta(30)):
            nuevo = pss(pag=i.pag, fecha=date.today(),
                        usu=i.usu, password=[pwd_generator()])
            introducir_clase(nuevo)


def delect(pag):
    elementos = buscar_todas()
    for i in elementos:
        if (i.pag == pag):
            delect_element(i.id)


def editar(pag, nuevo: str):
    elementos = buscar_todas()
    for i in elementos:
        if (i.pag == pag):
            update_element_usu(i.id, nuevo)


def asdict(clase):
    return {'fecha': clase.fecha,
            'usu': clase.usu,
            "pag": clase.pag,
            'password': clase.password[0],
            'act': clase.act,
            'id': clase.id}

