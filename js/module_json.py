import json

class json_ws:

    def __init__(self):
        self.caminho = 'ws_motos.json'

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