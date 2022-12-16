from datetime import datetime

def verifica_disciplina(disciplina, nome_disciplina=None):
    if not disciplina.Disciplinas['Disciplinas'].keys():
        print('\nNão existem disciplinas cadastradas ainda\n')
        return True

    elif nome_disciplina not in disciplina.Disciplinas['Disciplinas'].keys() and nome_disciplina != None:
        print('\nEsta disciplina não foi cadastrada\n')
        return True

    else:
        return False


def verifica_atividade(disciplina, nome_disciplina, nome_atividade, modelo='Cadastradas'):
    if modelo == 'Cadastradas':

        if nome_atividade in disciplina.Disciplinas['Disciplinas'][nome_disciplina]['Atividades'].keys():
            return True

    elif modelo == 'Não Cadastradas':

        if nome_atividade not in disciplina.Disciplinas['Disciplinas'][nome_disciplina]['Atividades'].keys():
            return True


def verifica_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')

    except ValueError:
        print('\nFormato Inválido\n')
        return True

    else:
        data = data.split('/')
        data = datetime(int(data[2]), int(data[1]), int(data[0]))

        if data < datetime.today():
            print('\nData inválida, passado!!!\n')
            return True

        else:
            return False


def filtra_data(disciplina, nome_disciplina):
    datas = []

    for atividade in disciplina.Disciplinas['Disciplinas'][nome_disciplina]['Atividades'].keys():
        datas.append(disciplina.Disciplinas['Disciplinas']
                     [nome_disciplina]['Atividades'][atividade]['Data Entrega'])

    return datas


if __name__ == "__main__":
    print('\nAviso!!!, você está executando um arquivo de funções, talvez o resultado que espera não seja encontrado\n')
