
class ordem_s:

    def __init__(self, data_entrada, data_saida, nome_cliente, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas):
        
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.nome_cliente = nome_cliente, 
        self.veiculo = veiculo, 
        self.desc = desc, 
        self.laudo_tecnico = laudo_tecnico, 
        self.forma_pagamento = forma_pagamento, 
        self.status = status, 
        self.valor_mao_obra = valor_mao_obra 
        self.valor_pecas = valor_pecas

    def __str__(self):
        return f'{self.data_entrada}-{self.data_saida}-{self.nome_cliente}-{self.veiculo}-{self.desc}-{self.laudo_tecnico}-{self.forma_pagamento}-{self.status}-{self.valor_mao_obra}-{self.valor_pecas}'