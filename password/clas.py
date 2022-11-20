from dataclasses import dataclass,field
from datetime import date
import uuid

def id_gen()-> str:
    return str(uuid.uuid4()) 

@dataclass
class pss:
    pag:str
    fecha:date
    usu:str
    password: list[str]=field(default_factory=list)
    act:bool=False
    id:str =field( default_factory=id_gen)
    ultima:bool=True


def transf_arr_clase (arry):
    if (isinstance(arry,tuple)):
        if (arry[5]==1):
            aux=True
        else:
            aux=False
        if (arry[6]==1):
            aux3=True
        else:
            aux3=False
        clase=pss(pag=arry[2],fecha=arry[4],usu=arry[1],password=[arry[3]],act=aux,id=arry[0],ultima=aux3 )
        return(clase)


    elif (isinstance(arry,list)):
        clase=[]
        for i in arry:
            if (i[5]==1):
                aux=True
            else:
                aux=False
            if (i[6]==1):
                aux3=True
            else:
                aux3=False
            aux2=pss(pag=i[2],fecha=i[4],usu=i[1],password=[i[3]],act=aux,id=i[0],ultima=aux3)
            clase.append( aux2)
        return(clase)