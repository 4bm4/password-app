from datetime import *
import random


def pwd_generator():
    capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "actual_dic", "Y", "Z"]
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "actual_dic", "y", "z"]
    simbols = ["!", "@", "#", "$", "%", "&", "/", "(" ")", "=", "?", "¡"]
    numb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    charact = capitals + minus + simbols + numb

    password = []
    for i in range(22): 
        random_char = random.choice(charact) 
        password.append(random_char)

    password = "".join(password) 
    return password


