from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from module_json import json_ws

class Tela_Editar_OS:

    def __init__(self, id):
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year
        self.data_atual = f'{self.day}/{self.month}/{self.year}'

        self.id = id
        
        # OBEJTO OS
        self.window()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.geometry('300x400')
        self.windowMain.title('EDITAR ORDEM DE SERVIÇO')

        # Data
        lblDataEntrada = Label(self.windowMain, text='Data de Entrada:')
        lblDataEntrada.place(x=10, y=10)

        etDataEntrada = Entry(self.windowMain)
        etDataEntrada.place(x=10, y=30)

        lblDataSaida = Label(self.windowMain, text='Data de Saida:')
        lblDataSaida.place(x=150, y=10)

        etDataSaida = Entry(self.windowMain)
        etDataSaida.place(x=150, y=30)

        # Cliente e Veiculo
        lblCliente = Label(self.windowMain, text='Cliente:*')
        lblCliente.place(x=10, y=60)

        etCliente = Entry(self.windowMain, font='Arial 10 bold', fg=f'{json_ws().getColorCliente()}', width=17)
        etCliente.place(x=10, y=80)

        lblVeiculo = Label(self.windowMain, text='Veiculo:*')
        lblVeiculo.place(x=150, y=60)

        etVeiculo = Entry(self.windowMain, font='Arial 10 bold', fg=f'{json_ws().getColorVeiculo()}', width=17)
        etVeiculo.place(x=150, y=80)

        # Descricao e Laudo
        lblDesc = Label(self.windowMain, text='Descrição do Cliente:')
        lblDesc.place(x=10, y=120)

        etDesc = Entry(self.windowMain)
        etDesc.place(x=10, y=140)

        lblLaudo = Label(self.windowMain, text='Laudo Tecnico:')
        lblLaudo.place(x=150, y=120)

        etLaudo = Entry(self.windowMain)
        etLaudo.place(x=150, y=140)

        # Pagamento
        lblPagamento = Label(self.windowMain, text='Forma de Pagamento:')
        lblPagamento.place(x=10, y=180)

        comboPagamento = ttk.Combobox(self.windowMain, width=17)

        comboPagamento['values'] = tuple(
            ['DINHEIRO', 'CARTÃO', 'PIX', 'OUTRO'])
        comboPagamento.current(0)
        comboPagamento.place(x=10, y=200)

        # Status
        lblStatus = Label(self.windowMain, text='Status:')
        lblStatus.place(x=150, y=180)

        comboStatus = ttk.Combobox(self.windowMain, width=17)

        comboStatus['values'] = tuple(
            ['EM ESPERA', 'EM ANDAMENTO', 'CONCLUIDO'])
        comboStatus.current(0)
        comboStatus.place(x=150, y=200)

        # Valores
        lblObra = Label(self.windowMain, text='Valor mão de Obra:')
        lblObra.place(x=10, y=240)

        etObra = Entry(self.windowMain)
        etObra.place(x=10, y=260)

        lblPecas = Label(self.windowMain, text='Valor em Peças:')
        lblPecas.place(x=150, y=240)

        etPecas = Entry(self.windowMain)
        etPecas.place(x=150, y=260)

        lblOutros = Label(self.windowMain, text='Outros Valores:')
        lblOutros.place(x=10, y=300)

        etOutros = Entry(self.windowMain)
        etOutros.insert(0, '0')
        etOutros.place(x=10, y=320)

        #Telefone
        lblTelefone = Label(self.windowMain, text='Telefone:')
        lblTelefone.place(x=150, y=300)

        etTelefone = Entry(self.windowMain, font='Arial 10 bold', fg=f'{json_ws().getColorTelefone()}', width=17)
        etTelefone.place(x=150, y=320)

        # Botões de Salvar e Cancelar
        btSalvar = Button(self.windowMain, text='SALVAR', width=16,
                          bg='SpringGreen', command=lambda: save())
        btSalvar.place(x=10, y=360)

        btVoltar = Button(self.windowMain, text='CANCELAR', width=16, bg='Tomato', command=lambda: exit())
        btVoltar.place(x=150, y=360)

        # Funcoes
        def save():

            # MENSAGEM DE ERROR
            if etVeiculo.get() == '' or etCliente.get() == '':
                messagebox.showerror(
                    'AVISO', 'CAMPOS OBRIGATÓRIOS NÃO ESTÃO PREENCHIDOS')

            else:
                # SALVAR
                if messagebox.askyesno('', 'EDITAR OS?'):

                    bd().updateOS(
                        self.id,
                        etDataEntrada.get(),
                        etDataSaida.get(),
                        etCliente.get().upper(),
                        etTelefone.get(),
                        etVeiculo.get().upper(),
                        etDesc.get().upper(),
                        etLaudo.get().upper(),
                        comboPagamento.get(),
                        comboStatus.get(),
                        float(etObra.get()),
                        float(etPecas.get()),
                        float(etOutros.get())
                    )

                    messagebox.showinfo('','EDITADO COM SUCESSO !')

                #FECHAR TELA
                self.windowMain.destroy()

        def clear():
            # LIMPAR
            etDataEntrada.delete(0, END)
            etDataSaida.delete(0, END)
            etCliente.delete(0, END)
            etVeiculo.delete(0, END)
            etDesc.delete(0, END)
            etLaudo.delete(0, END)
            etObra.delete(0, END)
            etPecas.delete(0, END)
            etOutros.delete(0, END)

        def exit():
            self.windowMain.destroy()

        def setDados():
            dados = bd().getOS(self.id)

            etDataEntrada.insert(0, dados[1])
            etDataSaida.insert(0, dados[2])
            etCliente.insert(0, dados[3])
            etTelefone.insert(0, dados[4])
            etVeiculo.insert(0, dados[5])
            etDesc.insert(0, dados[6])
            etLaudo.insert(0, dados[7])
            setPagamento(dados[8])
            setStatus(dados[9])
            etObra.insert(0, dados[10])
            etPecas.insert(0, dados[11])
            etOutros.insert(0, dados[12])

        def setPagamento(pag):

            for pos, i in enumerate(comboPagamento['values']):
                if i == pag:
                    comboPagamento.current(pos)

        def setStatus(status):
            for pos, i in enumerate(comboStatus['values']):
                if i == status:
                    comboStatus.current(pos)
        
        #SETAR DADOS
        setDados()

        self.windowMain.mainloop()