# Arquivo das Disciplinas

# Criando a Classe Disciplina
class Disciplina():
    def __init__(self):
        # Dicionário com todas as disciplinas/atividades
        self.Disciplinas = {'Disciplinas': dict()}

    # Função que incrementa uma nova disciplina no dicionário de disciplina
    def adicionar_nova_disciplina(self, nova_disciplina, nome_professor):
        self.Disciplinas['Disciplinas'].update({nova_disciplina.lower(
        ): {'Nome Professor': nome_professor, 'Atividades': dict()}})

        return f'\n{nova_disciplina.capitalize()} cadastro com êxito!\n'


if __name__ == "__main__":
    print('\nAviso!!!, você está executando a classe de disciplinas do software, talvez o resultado que espera não seja encontrado\n')
