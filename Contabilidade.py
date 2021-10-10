from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd

class Contabilidade:

    def __init__(self):
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year
        self.data_atual = f'{self.day}/{self.month}/{self.year}'

        self.id = id

        self.window()
        #self.login()

    def login(self):

        windowLogin = Tk()

        lblSenha = Label(windowLogin, text='Senha:')
        lblSenha.pack()

        etSenha = Entry(windowLogin, font='Arial 12 bold', show='*')
        etSenha.pack()

        def verify():
            
            if etSenha.get() == '3098':
                #DESTRUIR JANELA
                windowLogin.destroy()

                #CHAMAR CONTABILIDADE
                self.window()
            else:
                messagebox.showerror('', 'SENHA INCORRETA !')
                windowLogin.destroy()

        bt = Button(windowLogin, text='Entrar', command=verify)
        bt.pack()

        windowLogin.mainloop()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.title('CONTABILIDADE W MOTOS')
        self.windowMain.geometry('730x320')

        #Data
        lblData = Label(self.windowMain, text='Dia:')
        lblData.place(x=10, y=20)

        comboData = ttk.Combobox(self.windowMain, width = 8) 

        comboData['values'] = tuple(['{}'.format(i) for i in range(1, 32)])
        comboData.current(self.day-1)
        comboData.place(x=10, y=40)

        #Mes
        lblMes = Label(self.windowMain, text='Mês:')
        lblMes.place(x=130, y=20)

        comboMes = ttk.Combobox(self.windowMain, width = 8) 

        comboMes['values'] = tuple(['{}'.format(i) for i in range(1, 13)])
        comboMes.current(self.month-1)
        comboMes.place(x=130, y=40)

        #Ano
        lblAno = Label(self.windowMain, text='Ano:')
        lblAno.place(x=250, y=20)

        comboAno = ttk.Combobox(self.windowMain, width = 8) 

        comboAno['values'] = tuple(['{}'.format(i) for i in range(2021, 2051)])
        comboAno.current(self.year - 2021)
        comboAno.place(x=250, y=40)

        #CONTANIER
        lblContDia = Label(text='RECEITA DIA', font='Arial 15', width=20, height=2, bg='#fee440')
        lblContDia.place(x=10, y=80)

        contValorDia = Label(text='', font='Arial 15', width=20, height=2, bg='White')
        contValorDia.place(x=10, y=132)

        lblContMes = Label(text='RECEITA MÊS', font='Arial 15', width=20, height=2, bg='#00bbf9')
        lblContMes.place(x=250, y=80)

        contValorMes = Label(text='', font='Arial 15', width=20, height=2, bg='White')
        contValorMes.place(x=250, y=132)

        lblContTotal = Label(text='RECEITA TOTAL', font='Arial 15', width=20, height=2, bg='#00f5d4')
        lblContTotal.place(x=490, y=80)

        contValorTotal = Label(text='', font='Arial 15', width=20, height=2, bg='White')
        contValorTotal.place(x=490, y=132)

        #FORMA DE PAGAMENTO
        """lblContDinheiro = Label(text='DINHEIRO', font='Arial 15', width=20, height=2, bg='#ee6055')
        lblContDinheiro.place(x=10, y=232)

        contValorDinheiro = Label(text='', font='Arial 15', width=20, height=2, bg='White')
        contValorDinheiro.place(x=10, y=284)

        lblContCartao = Label(text='CARTÃO', font='Arial 15', width=20, height=2, bg='#60d394')
        lblContCartao.place(x=250, y=232)

        contValorCartao = Label(text='', font='Arial 15', width=20, height=2, bg='White')
        contValorCartao.place(x=250, y=284)

        lblContPix = Label(text='PIX/TED', font='Arial 15', width=20, height=2, bg='#aaf683')
        lblContPix.place(x=490, y=232)

        contValorPix = Label(text='', font='Arial 15', width=20, height=2, bg='White')
        contValorPix.place(x=490, y=284)"""

        def setValeusData():

            #RETORNA UMA LISTA [DIA, MES, TOTAL]
            d = f'{comboData.get()}/{comboMes.get()}/{comboAno.get()}'
            m = f'/{comboMes.get()}/{comboAno.get()}'

            values = bd().getContabilidadeGeral(d, m)

            #SETAR O VALOR TOTAL
            contValorTotal['text'] = f'R$ {values[2]:.2f}'

            #SETAR O VALOR MÊS
            contValorMes['text'] = f'R$ {values[1]:.2f}'
            
            #SETAR O VALOR DIA
            contValorDia['text'] = f'R$ {values[0]:.2f}'
        
        """def setValuesPagamento():
            #DINHEIRO
            contValorDinheiro['text'] = f'R$ {bd().getContabilidadeDinheiro():.2f}'

            #CARTAO
            contValorCartao['text'] = f'R$ {bd().getContabilidadeCartao():.2f}'

            #PIX
            contValorPix['text'] = f'R$ {bd().getContabilidadePix():.2f}'"""

        btConsultar = Button(text='CONSULTAR', font='Arial 15', bg='SpringGreen', width=18, height=2, command=setValeusData)
        btConsultar.place(x=250, y=232)

        #SETAR VALOR
        #setValeusData()
        #setValuesPagamento()

        self.windowMain.mainloop()

Contabilidade()