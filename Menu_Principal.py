from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os
from Contabilidade import Contabilidade
from showOS import consulta
from Tela_Cadastrar_OS import Tela_Cadastrar_OS
from Contabilidade import Contabilidade
from module_json import json_ws

class Menu_Principal:

    def __init__(self) -> None:
        self.window()

    def window(self):
        # Creating tkinter window
        window = Tk()
        window.geometry('993x480')
        window.title('CONSULTAR OS')

        # BARRA DE FUNÇÕES
        menubar = Menu(window, fg='Black')
        myMenu = Menu(menubar, tearoff=0)

        # MENU FILE
        fileMenuFile = Menu(myMenu, fg='Black')
        fileMenuFile.add_command(label='Nova', command=lambda:open('Nova'))
        fileMenuFile.add_command(label='Exibir', command=lambda:open('Exibir'))
        fileMenuFile.add_separator()
        fileMenuFile.add_command(label='Contabilidade', command=lambda:open('C_Total'))
        fileMenuFile.add_separator()
        fileMenuFile.add_command(
            label='Sair', command=lambda: window.destroy())

        menubar.add_cascade(label="ORDEM DE SERVIÇO", menu=fileMenuFile)

        #LOGO
        imagem = PhotoImage(file=f"{json_ws().getPathLogo()}")
        w = Label(window, image=imagem)
        w.imagem = imagem
        w.pack()

        #FECHAR MENU PARA CONTROLE DE TELAS
        def open(w):
            
            #FECHAR MENU
            window.destroy()

            if w == 'Nova':
                #ABRIR JANELA
                Tela_Cadastrar_OS()

                #REABRIR MENU
                Menu_Principal()

            elif w == 'Exibir':
                #ABRIR JANELA
                consulta()

                #REABRIR MENU
                Menu_Principal()
            
            elif w == 'C_Total':
                #ABRIR JANELA
                Contabilidade()

                #REABRIR MENU
                Menu_Principal()
                
        # configurar file menu
        window.config(menu=menubar)

        window.mainloop()
