import pyrebase

class bd:

    def __init__(self):

        self.config_os = {
            "databaseURL":"https://wmotos-oficina-default-rtdb.firebaseio.com/Ordem_Servico",
            "apiKey": "AIzaSyB5XWQIfNFKxTJD5rpyeW4xLxkzAG6Wdf0",
            "authDomain": "wmotos-oficina.firebaseapp.com",
            "projectId": "wmotos-oficina",
            "storageBucket": "wmotos-oficina.appspot.com",
            "messagingSenderId": "518714060401",
            "appId": "1:518714060401:web:84023ff73375212c82b5d0",
            "measurementId": "G-7BN59J39EF"
        };

        firebase = pyrebase.initialize_app(self.config_os)
        self.db = firebase.database()

        self.mao_de_obra_total = 0
        self.contabilidade_dia = 0
        self.contabilidade_mes = 0
        self.contabilidade_dinheiro = 0
        self.contabilidade_cartao = 0
        self.contabilidade_pix = 0

    def getId(self):
        oss = self.db.get().each()

        if oss == None:
            return 0

        return len(oss)

    def insertOS(self, data_entrada, data_saida, nome_cliente, telefone, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas, valor_outros):

        #PEGA O ULTIMO ID
        id = self.getId()

        # ADIDIONA VALOR NO DICIONÁRIO
        data = {
            'id': id,
            'data_entrada': data_entrada,
            'data_saida': data_saida,
            'nome_cliente': nome_cliente,
            'telefone': telefone,
            'veiculo': veiculo,
            'desc': desc,
            'laudo_tecnico': laudo_tecnico,
            'forma_pagamento': forma_pagamento,
            'status': status,
            'valor_mao_obra': valor_mao_obra,
            'valor_pecas': valor_pecas,
            'valor_outros': valor_outros
            }

        # SALVAR NO DICIONARIO
        self.db.child(id).set(data)

    def delOS(self, id):
        #APAGAR OS
        self.db.child(id).remove()

    def updateOS(self, id, data_entrada, data_saida, nome_cliente, telefone, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas, valor_outros):

        # ADIDIONA VALOR NO DICIONÁRIO
        data = {
            'id': id,
            'data_entrada': data_entrada,
            'data_saida': data_saida,
            'nome_cliente': nome_cliente,
            'telefone': telefone,
            'veiculo': veiculo,
            'desc': desc,
            'laudo_tecnico': laudo_tecnico,
            'forma_pagamento': forma_pagamento,
            'status': status,
            'valor_mao_obra': valor_mao_obra,
            'valor_pecas': valor_pecas,
            'valor_outros': valor_outros
            }

        # SALVAR NO DICIONARIO
        self.db.child(id).set(data)

    def updateAttrOS(self, id, attr, val):
        #ATUALIZAR ATRIBUTOS
        self.db.child(id).update({attr: val})

    def getAllOS(self):
        #LISTA DE OSs
        list_os = []

        for i in range(self.getId()):
            #PEGA A OS
            os = self.getOS(i)

            #ADICIONA A LISTA
            list_os.append(os)

        return list_os

    def getOS(self, id):

        data = {}
        os = self.db.child(int(id)).get().each()
        
        if os == None:
            return False

        for i in os:
            data[i.key()] = i.val()

        #CRIA UMA TUPLA
        tuple_os = (
            data['id'],
            data['data_entrada'],
            data['data_saida'],
            data['nome_cliente'],
            data['telefone'],
            data['veiculo'],
            data['desc'],
            data['laudo_tecnico'],
            data['forma_pagamento'],
            data['status'],
            data['valor_mao_obra'],
            data['valor_pecas'],
            data['valor_outros']
        )

        #RETORNA UMA DA OS
        return tuple_os

    def getNomeVeiculoOS(self, str):
        pass

    # --- CONTABILIDADE ---
    def getContabilidadeGeral(self, data, mes_atual):

        total_geral = 0
        dia = 0
        mes = 0

        for i in self.getAllOS():
            if i[9] == 'CONCLUIDO':
                total_geral += i[10]

            if i[9] == 'CONCLUIDO' and i[2] == data:
                dia += i[10]    

            if i[9] == 'CONCLUIDO' and mes_atual in i[2]:
                mes += i[10]

        return [dia, mes, total_geral]