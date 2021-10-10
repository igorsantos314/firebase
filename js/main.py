from tabulate import tabulate
from ordem_servico import os_ws

class  main:
    
    def menu(self):

        object_ = os_ws()

        menu_opc = [
            ('0','CADASTRAR'),
            ('1','EXIBIR TODAS'),
            ('2','EDITAR'),
            ('3','DELETAR')
            ]

        while True:
            #EXIBIR MENU
            print(tabulate(menu_opc, ['MENU'], tablefmt="pretty"))

            #PEGAR A OPÇÃO DO USUÁRIO
            opc = int(input('-> '))

            if opc == 0:
                object_.newOS()

            elif opc == 1:
                object_.showAll()

            elif opc == 2:
                object_.editOS()

            elif opc == 3:
                object_.delOS()

main().menu()

