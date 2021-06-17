import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from typing import ItemsView

from assunto import Assunto

class AssuntoView:

    def __init__(self,win):
        self.assuntoCRUD = Assunto()

        #Criar os componentes de tela
        self.temaLabel = tk.Label(win, text='Tema:') 
        self.temaEdit = tk.Entry(width = 32, bd=3)
        self.descricao_assuntoLabel = tk.Label(win, text='Descrição Assunto:') 
        self.descricao_assuntoEdit = tk.Entry(width = 32, bd=3)

        self.btnCadastrar = tk.Button(win,text = 'Cadastrar', width = 7, command=self._on_cadastrar_clicked)
        self.btnAlterar = tk.Button(win,text = 'Alterar', width = 7, command=self._on_atualizar_clicked)
        self.btnExcluir = tk.Button(win,text = 'Excluir', width = 7, command=self._on_deletar_clicked)

        self.assuntoList = ttk.Treeview(win, columns=(1,2,3), show='headings')
        self.verscrlbar = ttk.Scrollbar(win,orient="vertical", command=self.assuntoList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.assuntoList.configure(yscrollcommand = self.verscrlbar.set)

        self.assuntoList.heading(1, text='ID')
        self.assuntoList.heading(2, text='Tema')
        self.assuntoList.heading(3, text='Descrição Assunto')
        self.assuntoList.column(1, minwidth=0, width=50)
        self.assuntoList.column(2, minwidth=0, width=250)
        self.assuntoList.column(3, minwidth=0, width=400)
        self.assuntoList.pack()
        self.assuntoList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)


        #Posicionar os componentes na tela
        self.temaLabel.place(x=10,y=10)
        self.temaEdit.place(x=60,y=10)
        self.descricao_assuntoLabel.place(x=10,y=40)
        self.descricao_assuntoEdit.place(x=140,y=40)
        self.btnCadastrar.place(x=550,y=30)
        self.btnAlterar.place(x=650,y=30)
        self.btnExcluir.place(x=450,y=30)
        self.assuntoList.place(x=10,y=90)
        self.verscrlbar.place(x=710,y=90, height=222)

        self.carregar_dados_iniciais_treeView()

    def _on_mostrar_clicked(self, event):
        selection = self.assuntoList.selection()
        Item = self.assuntoList.item(selection)

        tema = Item["values"][1]
        descricao_assunto = Item["values"][2]

        self.temaEdit.delete(0, tk.END)
        self.temaEdit.insert(0, tema)
        self.descricao_assuntoEdit.delete(0, tk.END)
        self.descricao_assuntoEdit.insert(0, descricao_assunto)

    def carregar_dados_iniciais_treeView(self):
        registros = self.assuntoCRUD.consultar()

        count = 0
        for item in registros:
            id_assunto = item[0]
            tema = item[1]
            descricao_assunto = item[2]

            self.assuntoList.insert('','end',iid=count, values=(str(id_assunto),tema,descricao_assunto))
            count = count + 1


    def _on_cadastrar_clicked(self):
        #Recuperar os dados dos campos texto
        tema = self.temaEdit.get()
        descricao_assunto = self.descricao_assuntoEdit.get()

        #Chamar o cadastrar do assunto.py para cadastrar no banco
        if self.assuntoCRUD.cadastrar(tema, descricao_assunto):
            id_assunto =  self.assuntoCRUD.consultar_ultimo_id()
            #Atualizar a TreeView
            self.assuntoList.insert('','end',iid= (id+1), values=(str(id_assunto),tema, descricao_assunto))
            #Mostrar mensagem para usuário
            mb.showinfo("Mensagem", "Cadastro executado com sucesso!")
            #Limpar os campos texto
            self.temaEdit.delete(0,tk.END)
            self.descricao_assuntoEdit.delete(0,tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no cadastro!")
            #Retornando o foco
            self.temaEdit.focus_set()
            self.descricao_assuntoEdit.focus_set()

    def _on_atualizar_clicked(self):
        linhaSelecionada = self.assuntoList.selection()
      
        if len(linhaSelecionada) != 0:
            id_assunto = self.assuntoList.item(linhaSelecionada[0])["values"][0]
            tema = self.temaEdit.get()
            descricao_assunto = self.descricao_assuntoEdit.get()

            if  self.assuntoCRUD.atualizar(id_assunto,tema, descricao_assunto):

                self.assuntoList.item(self.assuntoList.focus(), values=(str(id_assunto),tema, descricao_assunto))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")
                self.temaEdit.delete(0, tk.END)
                self.descricao_assuntoEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")
                self.temaEdit.focus_set()
                self.descricao_assuntoEdit.focus_set()
    
    def _on_deletar_clicked(self):
        linhaSelecionada = self.assuntoList.selection()

        if len(linhaSelecionada) != 0:
            id_assunto = self.assuntoList.item(linhaSelecionada[0])["values"][0]

            if  self.assuntoCRUD.excluir(id_assunto):
                self.assuntoList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.temaEdit.delete(0, tk.END)
                self.descricao_assuntoEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                self.temaEdit.focus_set()
                self.descricao_assuntoEdit.focus_set()

#janela = tk.Tk()
#principal = AssuntoView(janela)
#janela.title("Cadastro de Assuntos")
#janela.geometry("950x400+0+0")
#janela.configure(background="#7FFFD4")
#janela.mainloop()