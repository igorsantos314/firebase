import os
import pyrebase

class data_base:

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

    def getId(self):
        oss = self.db.get().each()

        if oss == None:
            return 0

        return len(oss)

    def saveOS(self, data_entrada, data_saida, nome_cliente, telefone, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas):

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
            'valor_pecas': valor_pecas
            }

        # SALVAR NO DICIONARIO
        self.db.child(id).set(data)

    def getOS(self, id):

        data = {}
        os = self.db.child(int(id)).get().each()

        if os == None:
            return False

        for i in os:
            data[i.key()] = i.val()

        #RETORNA UM DICIONARIO DA OS
        return data

    def updateOS(self, id, attr, val):
        #ATUALIZAR ATRIBUTOS
        self.db.child(id).update({attr: val})

    def removeOS(self, id):
        #APAGAR OS
        self.db.child(id).remove()

#print(data_base().getOS())
#data_base().saveOS('1/1/2021', '1/1/2021', 'Maria', '81 982333074', 'BROS 150', '--', 'REVISÃO GERAL', 'DINHEIRO', 'CONCLUIDO', 70, 120)
#data_base().updateOS(0, 'telefone', '81 921212121')
#data_base().removeOS(0)
#data = {
#    'Name':'Rafa',
#    'Age':50
#}

#db.child('1').update({"Age":15, "Name":'Jose Santos'})

#db.child('3').set(data)
#db.child('Users').set(data)

#for i in db.get().each():
#    print(i.key())
#    print(i.val())