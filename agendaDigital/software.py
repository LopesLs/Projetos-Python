# Arquivo do Software

# Importando as classes e funções
from classes.homeworks import Atividades
from classes.materias import Disciplina
from functions.defs import *

# Instanciando as classes
disciplina = Disciplina()
atividade = Atividades()

# While contendo o menu
while True:
    print('-=-' * 19)
    print('                     MENU DE OPÇÕES        ')
    print('-=-' * 19)
    print()
    print('''  [1] - Adicionar disciplina           
  [2] - Adicionar atividade             
  [3] - Marcar atividades como concluídas     
  [4] - Listar atividades em aberto     
  [5] - Listar atividades concluídas    
  [6] - Sair da agenda digital''')
    print()
    print('-=-' * 19)

    # Tentando a opção do menu
    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("\nOpção inválida\n")
        continue

    if opcao == 1:
        nome_disciplina = input("\nQual disciplina deseja cadastrar? ").lower()

        # Verificando já existe uma discplina cadastrada com o mesmo nome
        if nome_disciplina in disciplina.Disciplinas['Disciplinas'].keys():
            print('\nDisciplina já cadastrada com o mesmo nome: ', nome_disciplina)

        else:
            nome_professor = input("Qual o nome do professor da disciplina? ")
            disciplina.Disciplinas = atividade.Disciplinas
            print(
                disciplina.adicionar_nova_disciplina(
                    nome_disciplina, nome_professor
                )
            )
            atividade.Disciplinas = disciplina.Disciplinas

    elif opcao == 2:
        # Verificando se existem disciplinas cadastradas
        if verifica_disciplina(disciplina):
            continue

        # Solicitando o nome da disciplina
        nome_disciplina = input(
            '\nInforme a disciplina na qual a atividade será lançada: ').lower()

        # Verificando se a disciplina informada foi cadastrada
        if verifica_disciplina(disciplina, nome_disciplina):
            continue

        # Solicitando o nome da atividade
        nome_atividade = input("Informe o conteúdo da atividade: ").lower()

        # Se já estiver uma atividade com este nome pare
        if verifica_atividade(atividade, nome_disciplina, nome_atividade):
            print('\nJá existe uma atividade com este nome\n')
            continue

        # Solicitando data da entrega
        data_entrega = input("Informe a data de entrega (d/m/a): ")

        # Verificando se a data é valida
        if verifica_data(data_entrega):
            continue

        # Filtrando do dicionário apenas as datas
        datas = filtra_data(atividade, nome_disciplina)

        # Se a data de entrega estiver na lista de datas
        if data_entrega in datas:
            print('\nJá existe uma atividade para este mesmo dia\n')

        else:
            atividade.adicionar_atividades(
                nome_disciplina, nome_atividade, data_entrega)
            print(f'\nAtividade {nome_atividade} enviada com sucesso\n')

    elif opcao == 3:
        # Solicitando o nome da disciplina
        nome_disciplina = input('Informe o nome da disciplina: ')

        # Verificando se existe o nome da disciplina
        if verifica_disciplina(disciplina, nome_disciplina):
            continue

        # Solicitando nome da atividade
        nome_atividade = input('Informe o nome da atividade: ')

        # Verificando se existe o nome da atividade
        if verifica_atividade(atividade, nome_disciplina, nome_atividade, 'Não Cadastradas'):
            print('\nAtividade não cadastrada\n')

        else:
            atividade.marcar_concluida(nome_disciplina, nome_atividade)
            print('\nAtividade marcada como concluída\n')

    elif opcao == 4:
        # Solicitando o nome da disciplina
        nome_disciplina = input('Informe o nome da disciplina: ')

        # Verificando se existe a disciplina
        if verifica_disciplina(disciplina, nome_disciplina):
            continue

        # Pegando a lista de atividades abertas
        atividades = atividade.visualizar_atividades(
            nome_disciplina, 'Abertas')

        # Se tiver conteúdo dentro de atividades mostre-pra gente
        if atividades:
            print('\nAtividades Abertas\n')
            for atv in atividades:
                print(atv)

        else:
            print('\nNão existem atividades abertas\n')

    elif opcao == 5:
        # Solicitando o nome da disciplina
        nome_disciplina = input('Informe o nome da disciplina: ')

        # Verificando se existe o nome da disciplina
        if verifica_disciplina(disciplina, nome_disciplina):
            continue

        # Pegando lista de atividades concluídas
        atividades = atividade.visualizar_atividades(
            nome_disciplina, 'Concluídas')

        # Se tiver conteúdo dentro da lista então mostre-nos
        if atividades:
            print('\nAtividades Concluídas\n')
            for atv in atividades:
                print(atv)

        else:
            print('\nNão existem atividades concluídas\n')

    elif opcao == 6:
        print('\nVocê saiu da agenda ^^\n')
        break
    
    #Opção apenas para desenvolvedores consultarem o dicionário de disciplinas enquanot testam o código
    elif opcao == 20211230013:
        print(atividade.Disciplinas)
        
    else:
        print('\nNão existe esta opcão\n')

