import json
import os

class json_ws:

    def __init__(self):
        self.caminho = 'ws_motos_config.json'
        self.dict = self.ler()

    def ler(self):
        #LER ARQUIVO
        with open(self.caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def escrever(self, dict):
        #ESCREVER DICIONÁRIO NO JSON
        with open(self.caminho, 'w', encoding='utf-8') as f:
            json.dump(dict, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

    def atualizar(self):
        #PEGAR JSON E SALVA EM UM DICT
        self.dict_finance = self.ler()

    def getPathLogo(self):
        return f"{os.getcwd()}/{self.dict['path_logo']}"

    def getPathBd(self):
        return f"{os.getcwd()}/{self.dict['path_bd']}"

    def getColorCliente(self):
        return self.dict['color_cliente']

    def getColorVeiculo(self):
        return self.dict['color_veiculo']

    def getColorTelefone(self):
        return self.dict['color_telefone']