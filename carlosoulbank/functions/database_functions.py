import sqlite3
from .security_functions import criptografar
from typing import Any

def conectar(nomeBanco:str):
    database = sqlite3.connect(nomeBanco)
    return database

def verificar_login(nome_conta : str, senha : str, bancodeDados : list[tuple[Any]]) -> bool:
    """
    DocString
        --> Uma vez que a função for solicitada, irá verificar se usuário existe no banco de dados e irá retornar um Boolean Value (True/False)
      
        Função criada por Carlos Eduardo.
    """
    
    for nomesenha in bancodeDados:
        if nome_conta in nomesenha:
            if criptografar(senha) in nomesenha:
                return True

    return False      
    

if __name__ == "__main__":
    print('\nAtenção!, você está executando um arquivo com as funcionalides do banco de dados para executar o arquivo principal, talvez o resultado que espere não seja atendido.\n')