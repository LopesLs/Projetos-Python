# Chamando funções
from functions.database_functions import *
from functions.security_functions import *
from functions.menu_display import *

# Conectando ao banco de dados e criando o cursor
database = conectar('Banco.db')
cursor = database.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS contas (nome TEXT PRIMARY KEY, senha TEXT, saldo REAL)")

print(f"\nBem vindos ao nosso banco Carlos SoulBank para poder ter acesso completo ao sistema, crie uma conta. Entrada as {mostrar_hora()}.\n\nINFO: Lembre-se que isso é um algoritmo simples que simula um banco, então todas as criações de contas infelizmente ainda são localmente\n")

while True:
    mostrar_menu_inicial()

    try:
        opcao = int(input("\nDigite sua opção: "))
    except ValueError:
        print(f"\nInforme as opção em números!\n")
        continue

    if opcao == 1:
        print("\nInfo: Opção Criar Conta foi escolhida com sucesso!")
        print("""\nRegras do Banco sobre a opção criar conta

A opção de Criar Conta deve receber:
- Nome de usuário
- senha (5 dígitos)""")

        conta = input("\nInforme o nome do usúario: ")
        nomes = []

        cursor.execute('SELECT nome from contas')

        for nome in cursor.fetchall():
            nomes.append(nome[0])

        if conta in nomes:
            print("\nOlá já existe um usuário com esse mesmo nome, tente outro.\n")
            continue

        else:
            senha = input("Informe a Senha: ")

            if len(senha) != 5:
                print("\nSenha permitida até 5 digitos!")

            else:
                cursor.execute(
                    f"INSERT INTO contas VALUES ('{conta}', '{criptografar(senha)}', 0)")
                database.commit()

                print("\nConta criada com sucesso!\n")

    elif opcao == 2:
        conta = input("\nInforme o nome do usuário: ")
        senha = input("\nInforme a Senha: ")
        cursor.execute('SELECT nome, senha FROM contas')

        if verificar_login(conta, senha, cursor.fetchall()):
            print(f'\nlogado como {conta}!\n')

            while True:
                mostrar_menu_in_account()

                try:
                    opcao = int(input("\nDigite sua opção: "))
                
                except ValueError:
                    print(f"\nInforme as opção em números!\n")
                    continue

                if opcao == 1:
                    print("\nInfo: Opção Visualizar conta foi escolhida com sucesso!")

                    saldo = cursor.execute(
                        f"SELECT saldo FROM contas WHERE conta = '{conta}' ")

                    print(f"\nInformações Da Conta\n"
                          f"Conta: {conta}\n"
                          f"Saldo: {saldo}\n")

                elif opcao == 2:
                    print("\nInfo: Opção Excluir Conta foi escolhida com sucesso!\n")

                    conta = input(
                        "Por favor, informe o nome de usúario da conta que deseja apagar: ")
                    contas = cursor.execute('SELECT nome FROM contas')
                    senhas = cursor.execute('SELECT senha FROM contas')

                    if conta in contas:
                        print("\nConta encontrada com êxito!")

                        senha = input("\nInforme sua senha: ")
                        senha = criptografar(senha)

                        if senha in senhas:
                            confirmacao = input(
                                "\nTem certeza que quer excluir?[S/N] ").lower()

                            if "si" in confirmacao:
                                cursor.execute(
                                    f"DELETE FROM contas WHERE conta = '{conta}' ")
                                database.commit()
                                print("\nA sua conta foi apagada com sucesso!\n")

                            elif "n" in confirmacao:
                                print("\nVocê será redirecionado pro menu\n")
                                continue

                        else:
                            print('Senha inválida')

                    else:
                        print("\nInfo: Não foi possível encontrar o usuario!")

                elif opcao == 3:
                    print("\nInfo: Opção Fazer Déposito escolhida foi com sucesso!")
                    print("""\nRegras do Banco sobre a opção fazer déposito

            A opção Depositar deve obedecer:
            - limite de 5000 mil por cada depósito
            - Valores negativos não podem ser depositados""")

                    deposito = float(
                        input("\nInforme a quantia que deseja depositar: "))

                    if deposito > 5000 or deposito < 0:
                        print(
                            "\nValor do depósito foi excedido, leia novamente as regras!")

                        print("""\nRegras do Banco sobre a opção fazer déposito

            A opção Depositar deve obedecer:
            - limite de 5000 mil por cada depósito
            - Valores negativos não podem ser depositados""")

                    else:
                        saldo = cursor.execute(
                            "SELECT saldo FROM contas WHERE nome = '{conta}'")
                        deposito += saldo.fetchall()[0][0]

                        cursor.execute(
                            f"UPDATE contas SET saldo = {deposito} WHERE conta = '{conta}' ")

                        database.commit()
                        print("\nInfo: O depósito foi efetuado com sucesso!\n")

                elif opcao == 4:
                    print("\nInfo: Opção Sacar o Money foi escolhida com sucesso!")
                    print("""\nRegras do Banco sobre a opção sacar o money:

            A opção de Saque deve obedecer:
            - Limite de 1000 por saque.
            - valores negativos não podem ser sacados.
            - Verifique o saldo da sua conta, para realizar o saque.""")
                    saque = float(
                        input("\nInforme a quantia que deseja sacar: "))

                    saldo = cursor.execute(
                        "SELECT saldo FROM contas WHERE conta = '{conta}'")

                    if saque > 1000:
                        print(
                            "\nValor do saque foi excedido, leia novamente as regras!")

                    elif saque > saldo.fetchall()[0][0]:
                        print(
                            "\nInfo: Saldo Insuficiente !!!")
                        continue

                    elif saque < 0:
                        print(
                            "\nInfo: Valor negativo informado, leia novamente as regras!")

                    else:
                        saldo.fetchall()[0][0] -= saque

                        cursor.execute(
                            f"UPDATE contas SET saldo = {saldo} WHERE conta = '{conta}' ")
                        database.commit()

                        print("\nInfo: O saque foi efetuado com sucesso!\n")

                elif opcao == 5:
                    print('\nVocê saiu da sua conta\n')
                    break

                else:
                    print(
                        "\nPara cada opção existe um número, preste atenção na tabela!\n")
        else:
            print('\nNão encontramos sua conta, revise os dados informados e tente novamente.\n')

    elif opcao == 3:
        print('\nNós sentimos muito se causamos desconfortos com nosso software, \nvocê pode enviar um email para lopes.carlos@academico.ifpb.edu.br iremos responder o mais rápido que pudermos\n')

    elif opcao == 4:
        break

    else:
        print('\nNão existe esta opção no nosso menu :), reveja com cuidado!\n')

print(
    f"\nNós da Carlos SoulBank agradeçemos pela preferência. Saída as {mostrar_hora()}.")
