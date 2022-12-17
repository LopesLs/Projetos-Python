from datetime import datetime

def criptografar(senha):
    """
    DocString
    --> Quando essa função é ativa, ele pega qualquer frase que o usuário digitir e codifica utilizando a cifra R
    Os dados do usuário são armazenados em um banco de dados onde pessoas podem ter acesso facilmente, então a codificação se torna importante.

    :param senhacodificada: Esse parâmetro, ele pode ser qualquer um, só depende do que o usuário informar.
    :return: tradutor: Ele quem faz o papel de tranformar as letras do alfabeto normal em aleátorias, só quem sabe da chave vai conseguir decifrar.
        Função criada por Carlos Eduardo.
    """

    tradutor = ""
    for letra in senha:
        if letra in "Aa": tradutor += "q"
        elif letra in "Bb": tradutor += "w"
        elif letra in "Cc": tradutor += "e"
        elif letra in "Dd": tradutor += "r"
        elif letra in "Ee": tradutor += "t"
        elif letra in "Ff": tradutor += "y"
        elif letra in "Gg": tradutor += "u"
        elif letra in "Hh": tradutor += "i"
        elif letra in "Ii": tradutor += "o"
        elif letra in "Jj": tradutor += "p"
        elif letra in "Kk": tradutor += "a"
        elif letra in "Ll": tradutor += "s"
        elif letra in "Mm": tradutor += "d"
        elif letra in "Nn": tradutor += "f"
        elif letra in "Oo": tradutor += "g"
        elif letra in "Pp": tradutor += "h"
        elif letra in "Qq": tradutor += "j"
        elif letra in "Rr": tradutor += "k"
        elif letra in "Ss": tradutor += "l"
        elif letra in "Tt": tradutor += "z"
        elif letra in "Uu": tradutor += "x"
        elif letra in "Vv": tradutor += "c"
        elif letra in "Ww": tradutor += "v"
        elif letra in "Xx": tradutor += "b"
        elif letra in "Yy": tradutor += "n"
        elif letra in "Zz": tradutor += "m"
        else: tradutor += letra
    return tradutor

def mostrar_hora():
    data = datetime.now()
    databr = data.strftime('%H:%M')
    return databr