from tkinter import ttk 
from tkinter import *
from Persistencia import bd
from module_print import print_document
from tkinter import messagebox
from Tela_Editar_OS import Tela_Editar_OS

class consulta:

    def __init__(self) -> None:
        self.window()

    def window(self):
        # Creating tkinter window 
        window = Tk()
        window.geometry('993x480')
        window.title('CONSULTAR OS')

        #BARRA DE FUNÇÕES
        menubar = Menu(window, fg='Black')
        myMenu = Menu(menubar, tearoff=0)

        #MENU FILE
        fileMenuFile = Menu(myMenu, fg='Black')
        fileMenuFile.add_command(label='Editar', command=lambda:editar())
        fileMenuFile.add_command(label='Excluir', command=lambda:deletar())
        fileMenuFile.add_separator()
        fileMenuFile.add_command(label='Imprimir', command=lambda:imprimir())
        
        menubar.add_cascade(label="File", menu=fileMenuFile)

        #BUSCAR
        lblBuscar = Label(window, text='BUSCAR:')
        lblBuscar.place(x=10, y=10)

        etBuscar = Entry(window, width=80)
        etBuscar.place(x=80, y=10)

        btBuscar = Button(window, text='BUSCAR', width=16,
                          bg='SpringGreen', command=lambda: buscar())
        btBuscar.place(x=590, y=8)

        #TREEVIEW
        style = ttk.Style(window)
        style.theme_use('clam')

        style.configure(    "Treeview",
                            background="Silver",
                            fieldbackground='Silver'
                            )

        style.map("Treeview", background=[('selected', 'SpringGreen')], foreground=[('selected', 'black')])

        # Using treeview widget 
        treev2 = ttk.Treeview(window, selectmode ='browse', height=20) 

        # Calling pack method w.r.to treeview 
        treev2.place(x=10, y=40)

        # Constructing vertical scrollbar 
        # with treeview 
        verscrlbar = ttk.Scrollbar(window, 
                                orient ="vertical", 
                                command = treev2.yview) 

        # scrollbar 
        verscrlbar.pack(side ='right', fill ='x') 

        # Configuring treeview 
        treev2.configure(xscrollcommand = verscrlbar.set) 

        # Defining number of columns 
        treev2["columns"] = ("1", "2", "3", "4", "5", "8", "9", "10", "11") 

        # Defining heading 
        treev2['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treev2.column("1", width = 60, anchor ='c') 
        treev2.column("2", width = 90, anchor ='se') 
        treev2.column("3", width = 90, anchor ='se') 
        treev2.column("4", width = 120, anchor ='se')
        treev2.column("5", width = 90, anchor ='se') 
        #treev2.column("6", width = 150, anchor ='se')
        #treev2.column("7", width = 150, anchor ='se') 
        treev2.column("8", width = 150, anchor ='se')
        treev2.column("9", width = 120, anchor ='se') 
        treev2.column("10", width = 120, anchor ='se')
        treev2.column("11", width = 120, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treev2.heading("1", text ="Id") 
        treev2.heading("2", text ="Data Entrada") 
        treev2.heading("3", text ="Data Saida")
        treev2.heading("4", text ="Cliente")
        treev2.heading("5", text ="Veiculo")
        #treev2.heading("6", text ="Descrição")
        #treev2.heading("7", text ="Laudo Tecnico")
        treev2.heading("8", text ="Forma de Pagamento")
        treev2.heading("9", text ="Status")
        treev2.heading("10", text ="Valor Mão de Obra")
        treev2.heading("11", text ="Valor de Peças")

        def getId():
            if len(treev2.selection()) == 0:
                messagebox.showwarning('','POR FAVOR SELECIONE UMA OS')
                
                #USUARIO N CLICOU
                return -1
            else:
                itemSelecionado = treev2.selection()[0]

                #PEGAR VALORES
                id = int(treev2.item(itemSelecionado, "values")[0])
                
                return id
            #Deletar Item
            #treev2.delete(itemSelecionado)

        def getAll():
            #VARRER LISTA E ADICIONAR NA TABELA
            for i in bd().getAllOS():
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], i[5], i[8], i[9], i[10], i[11]))

        def buscar():
            
            #LIMPA A TABELA
            limparTabela()

            #VARRER LISTA E ADICIONAR NA TABELA
            for i in bd().getNomeVeiculoOS(etBuscar.get().upper()):
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], i[5], i[8], i[9], i[10], i[11]))

        def imprimir():
            
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id > -1:
                #PEGAR A TUPLA
                conteudo = bd().getOS(id)

                #IMPRIMIR
                print_document(conteudo)
        
        def editar():
            
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id > -1:
                print(id)
                #FECHHA A JANELA
                window.destroy()

                #ABRE JANELA DE EDITAR
                Tela_Editar_OS(id)

                #REABRE A TELA DE EXIBIR
                consulta()

        def deletar():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:

                if messagebox.askyesno('', 'DESEJA APAGAR A OS?') == True:
                    #APGAR NO BANCO DE DADOS
                    bd().delOS(id)

                    messagebox.showinfo('','DELETADO COM SUCESSO!')

            #LIMPA TUDO
            limparTabela()

            #CARREGA ALTERAÇÕES
            getAll()

        def limparTabela():
            treev2.delete(*treev2.get_children())

        #Povoar Tabela
        getAll()

        #configurar file menu
        window.config(menu=menubar)

        # Calling mainloop 
        window.mainloop()