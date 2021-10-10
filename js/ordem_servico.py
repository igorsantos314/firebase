from tabulate import tabulate
from module_json import json_ws
from module_print import print_document


class os_ws:

    def __init__(self):
        self.dict = json_ws().ler()

        self.opc_pagamento = [('0', 'DINHEIRO'), ('1', 'CARTÃO'), ('2', 'PIX')]
        self.opc_status = [('0', 'EM_ESPERA'),
                           ('1', 'EM_ANDAMENTO'), ('2', 'CONCLUIDO')]

        # SETAR TITULO DA TABELA
        self.headers = [
            'ID',
            'ENTRADA',
            'SAIDA',
            'CLIENTE',
            'VEICULO',
            'DESCRICÃO',
            'LAUDO TECNICO',
            'PAGAMENTO',
            'STATUS',
            'VALOR M. OBRA',
            'VALOR PEÇAS'
        ]

        self.parametros = [
            'data_entrada',
            'data_saida',
            'nome_cliente',
            'veiculo',
            'desc',
            'laudo_tecnico',
            'forma_pagamento',
            'status',
            'valor_mao_obra',
            'valor_pecas'
        ]

    def exibirTitulo(self, titulo):
        # EXIBIR O TITULO PARA UMA ENTRADA
        list = [([titulo])]
        print(tabulate(list, tablefmt="pretty"))

    def exibir(self, list):
        print(tabulate(list, tablefmt="pretty"))

    def newOS(self):

        self.exibirTitulo('DIGITE OS NOVOS DADOS PARA A OS')

        data_entrada = input('Data Entrada:         ')
        data_saida = input('Data Saída:           ')
        nome_cliente = input('Nome do Cliente:      ').upper()
        veiculo = input('Veiculo:              ').upper()
        desc = input('Descrição do Cliente: ').upper()
        laudo_tecnico = input('Laudo Tecnico:        ').upper()

        self.exibir(self.opc_pagamento)
        forma_pagamento = int(input('Forma de Pagamento:   '))
        forma_pagamento = self.opc_pagamento[forma_pagamento][1]

        self.exibir(self.opc_status)
        status = int(input('Status:               '))
        status = self.opc_status[status][1]

        valor_mao_obra = input('Valor Mão de Obra:    ')
        valor_pecas = input('Valor Peças:          ')

        # ENVIAR DADOS PARA SALVAR
        self.saveOS(data_entrada, data_saida, nome_cliente, veiculo, desc,
                    laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas)

    def saveOS(self, data_entrada, data_saida, nome_cliente, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas):

        # CHAVE
        key = "OS"

        # ADIDIONA VALOR NO DICIONÁRIO
        self.dict[key][str(len(self.dict[key]))] = {'data_entrada': data_entrada,
                                                    'data_saida': data_saida,
                                                    'nome_cliente': nome_cliente,
                                                    'veiculo': veiculo,
                                                    'desc': desc,
                                                    'laudo_tecnico': laudo_tecnico,
                                                    'forma_pagamento': forma_pagamento,
                                                    'status': status,
                                                    'valor_mao_obra': valor_mao_obra,
                                                    'valor_pecas': valor_pecas
                                                    }

        # SALVAR DICIONÁRIO
        json_ws().escrever(self.dict)

        self.exibirTitulo("SALVO COM SUCESSO !!")

    def showAll(self):

        # LISTA DE EXIBIÇÃO
        list = []

        key = 'OS'

        for item in self.dict[key]:

            # PEGAR DICIONARIO DE VALORES
            values = self.dict[key][item]

            # ADICIONAR TUPLA NA LISTA DE EXIBIÇÃO
            list.append((item,
                         values['data_entrada'],
                         values['data_saida'],
                         values['nome_cliente'],
                         values['veiculo'],
                         '...',
                         '...',
                         values['forma_pagamento'],
                         values['status'],
                         values['valor_mao_obra'],
                         values['valor_pecas']))

        print(tabulate(list, self.headers))

    def setNewValues(self, item, edit, newValue):
        # EDITAR ITEM
        self.dict['OS'][item][edit] = newValue

        print(self.dict)

        # SALVAR DICIONÁRIO
        json_ws().escrever(self.dict)

    def editOS(self):

        # EXIBIR TODOS
        self.showAll()

        self.exibirTitulo('ESOLHA UMA OS PARA EDITAR')

        # PEGAR A OPCAO
        item = input('-> ')

        if item != '':

            # GERAR LISTA DE TUPLA COM NUMEROS
            list_edit = [(pos, i) for pos, i in enumerate(self.headers)]
            self.exibir(list_edit)

            # O QUE DESEJA EDITAR
            edit = int(input('-> '))

            # TEXTO
            self.exibirTitulo(f'EDITAR {self.headers[edit]}')

            if edit != '':
                # NOVO VALOR DA CHAVE
                newValue = input('-> ').upper()

                self.setNewValues(item, self.parametros[edit-1], newValue)

                # TEXTO
                self.exibirTitulo('EDITADO COM SUCESSO !')

    def delOS(self):

        # EXIBIR TODAS AS OS
        self.showAll()

        # TEXTO
        self.exibirTitulo('DIGITE O ID PARA DELETAR')

        id = input('-> ')

        if id != '':
            self.dict['OS'].pop(id)

            # SALVAR DICIONÁRIO
            json_ws().escrever(self.dict)

            # TEXTO
            self.exibirTitulo('DELETADO COM SUCESSO !')

    def print_os(self, item):

        # PEGAR DICIONARIO DE VALORES
        values = self.dict['OS'][item]

        # ADICIONAR TUPLA NA LISTA DE EXIBIÇÃO
        os = (
            item,
            values['data_entrada'],
            values['data_saida'],
            values['nome_cliente'],
            values['veiculo'],
            values['desc'],
            values['laudo_tecnico'],
            values['forma_pagamento'],
            values['status'],
            values['valor_mao_obra'],
            values['valor_pecas']
        )

        print_document(os)
