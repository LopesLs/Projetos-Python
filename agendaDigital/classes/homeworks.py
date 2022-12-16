# Arquivo das Atividades

from .materias import Disciplina


class Atividades(Disciplina):
    def __init__(self):
        super().__init__()

    # Função que adicona atividades, relacionando elas como elemento da chave disciplina
    def adicionar_atividades(self, nome_disciplina, titulo_atividade, data_entrega):
        self.Disciplinas['Disciplinas'][nome_disciplina]['Atividades'].update(
            {titulo_atividade: {'Data Entrega': data_entrega, "Status": 'Aberta'}})

    # Função que marca atividades como concluída
    def marcar_concluida(self, nome_disciplina, titulo_atividade):
        self.Disciplinas['Disciplinas'][nome_disciplina]['Atividades'][titulo_atividade]['Status'] = 'Concluída'

    # Função visualizar atividades
    def visualizar_atividades(self, nome_disciplina, status):
        # Lista Armazendo as atividades, elas podem ser as concluídas ou as pendentes.
        lista_atividades = []

        # Verificando as atividades pendentes
        if status == 'Abertas':
            # Percorrendo a lista de Disciplinas atrás do seu status de pendente
            for atividades in self.Disciplinas['Disciplinas'][nome_disciplina]['Atividades']:
                if self.Disciplinas['Disciplinas'][nome_disciplina]['Atividades'][atividades]['Status'] == 'Aberta':
                    lista_atividades.append(atividades)

        # Verificando status das concluídas
        elif status == 'Concluídas':
            # Percorrendo a lista de Disciplinas atrás do seu status
            for atividades in self.Disciplinas['Disciplinas'][nome_disciplina]['Atividades']:
                if self.Disciplinas['Disciplinas'][nome_disciplina]['Atividades'][atividades]['Status'] == 'Concluída':
                    lista_atividades.append(atividades)

        return lista_atividades


if __name__ == "__main__":
    print('\nAviso!!!, você está executando a classe de atividades do software, talvez o resultado que espera não seja encontrado\n')
