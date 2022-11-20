import random


def pwd_generator():
    capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
    simbols = ["!", "@", "#", "$", "%", "&", "/", "(",")", "=", "?", "¡"]
    numb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    charact = capitals + minus + simbols + numb

    password1 = []
    password2 = []
    password3 = []
    for i in range(1,7): 
        random_char = random.choice(charact) 
        password1.append(random_char)

    for i in range(1,7): 
        random_char = random.choice(charact) 
        password2.append(random_char)

    for i in range(1,7): 
        random_char = random.choice(charact) 
        password3.append(random_char)  

    password1 = "".join(password1) 
    password2 = "".join(password2) 
    password3 = "".join(password3)

    password= password1+"-"+password2+"-"+password3
    
    return password


