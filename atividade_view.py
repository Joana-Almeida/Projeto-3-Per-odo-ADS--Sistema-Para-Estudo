import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from typing import ItemsView

from atividade import Atividade
from assunto import Assunto


class AtividadeView:

    def __init__(self, win):
        self.atividadeCRUD = Atividade()

        self.astSelected = None
        self.astResult = None

        self.assuntoLabel = tk.Label(win, text='Assunto')
        self.assuntoEdit = ttk.Combobox(win, values=[])
        self.assuntoEdit.bind("<<ComboboxSelected>>", self._on_combo_changed)
        self.popular_combo_assunto()

        self.nome_atividadeLabel = tk.Label(win, text='Atividade')
        self.nome_atividadeEdit = tk.Entry(win)

        self.descricao_atividadeLabel = tk.Label(win, text='Descricao')
        self.descricao_atividadeEdit = tk.Entry(win)

        self.periodo_estudoLabel = tk.Label(win, text='Periodo')
        self.periodo_estudoEdit = tk.Entry(win)

        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self._on_cadastrar_clicked,  width = 8) 
        #self.btnExcluir = tk.Button(win, text='Excluir', command=self._on_deletar_clicked,  width = 8)     
        self.btnAlterar = tk.Button(win, text='Alterar', command=self._on_atualizar_clicked,  width = 8)   
         
        self.atividadeList = ttk.Treeview(win, columns=("ID", "Atividade", "Descrição", "Periodo"), selectmode='browse')

        self.atividadeList.heading("id_atividade", text="ID")
        self.atividadeList.heading("nome_atividade", text="Atividade")
        self.atividadeList.heading("descricao_atividade", text="Descrição")  
        self.atividadeList.heading("periodo_estudo", text="Periodo")  

        self.atividadeList.column("id_atividade",minwidth=0,width=100)
        self.atividadeList.column("nome_atividade",minwidth=0,width=100)
        self.atividadeList.column("descricao_atividade",minwidth=0,width=150)
        self.atividadeList.column("periodo_estudo",minwidth=0,width=125)

        self.atividadeList.pack(padx=10, pady=10)
        self.atividadeList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)

        self.verscrlbar = ttk.Scrollbar(win,orient="vertical",command=self.atividadeList.yview)        
        self.verscrlbar.pack(side ='right', fill ='x')
        self.atividadeList.configure(yscrollcommand=self.verscrlbar.set) 

        self.assuntoLabel.place(x=10, y=15)
        self.assuntoEdit.place(x=120, y=10)
        self.nome_atividadeLabel.place(x=10, y=55)
        self.nome_atividadeEdit.place(x=60, y=50)
        self.descricao_atividadeLabel.place(x=235, y=55)
        self.descricao_atividadeEdit.place(x=290, y=50)
        self.periodo_estudoLabel.place(x=470, y=55)
        self.periodo_estudoEdit.place(x=520, y=50)
        self.btnCadastrar.place(x=700, y=50)
        self.btnAlterar.place(x=700, y=80)
        self.atividadeList.place(x=10, y=90)
        self.verscrlbar.place(x=680, y=90, height=200)  

        
        self.carregar_dados_iniciais_treeView()


    def popular_combo_assunto(self):
        assunto=Assunto()
        self.astResult=assunto.consultar()
        if (len(self.astResult) > 0):

            self.astSelected = self.astResult[0][0]

            for registro in self.astResult:
                self.assuntoEdit['values']= (*self.assuntoEdit['values'], registro[1])

            self.assuntoEdit.current(0)  
      

    def carregar_dados_iniciais_treeView(self):
        if (self.astSelected != None):
            resultado = self.atividadeCRUD.consultar_por_assunto(self.astSelected)
            self.atividadeList.delete(*self.atividadeList.get_children())
            count = 0 
            for registro in resultado:
                self.atividadeList.insert('', 'end',iid=count,values=(str(registro[0]),registro[1],registro[2],registro[3]))  
                count = count + 1

    def _on_mostrar_clicked(self,event):
        selection = self.atividadeList.selection()
        item = self.atividadeList.item(selection[0])

        nome_atividade = item["values"][1]
        descricao_atividade = item["values"][2]
        periodo_estudo = item["values"][3]


        self.nome_atividadeEdit.delete(0, tk.END)
        self.nome_atividadeEdit.insert(0,nome_atividade)

        self.descricao_atividadeEdit.delete(0, tk.END)
        self.descricao_atividadeEdit.insert(0,descricao_atividade)

        self.periodo_estudoEdit.delete(0, tk.END)
        self.periodo_estudoEdit.insert(0,periodo_estudo)



    def _on_cadastrar_clicked(self):
        nome_atividade = self.nome_atividadeEdit.get() 
        descricao_atividade = self.descricao_atividadeEdit.get()
        periodo_estudo = self.periodo_estudoEdit.get()

        if self.atividadeCRUD.cadastrar(nome_atividade,descricao_atividade,periodo_estudo,self.astSelected):
            numeroLinhas = len(self.atividadeList.get_children())
            id_atividade = self.atividadeCRUD.consultar_ultimo_id()

            self.atividadeList.insert('','end',iid = numeroLinhas, values=(str(id_atividade),nome_atividade,descricao_atividade,periodo_estudo))
    
            mb.showinfo("Mensagem", "Cadastro executado com sucesso.")       
            self.nome_atividadeEdit.delete(0, tk.END)
            self.descricao_atividadeEdit.delete(0, tk.END)
            self.periodo_estudoEdit.delete(0, tk.END)
            self.nome_atividadeEdit.focus_set()
        else:
            mb.showinfo("Mensagem", "Erro no cadastro.") 
            self.nome_atividadeEdit.focus_set()



    def _on_atualizar_clicked(self):
        linhaSelecionada = self.atividadeList.selection()
      
        if len(linhaSelecionada) != 0:
            id_atividade = self.atividadeList.item(linhaSelecionada[0])["values"][0]
            nome_atividadeEdit = self.nome_atividadeEdit.get()
            descricao_atividadeEdit = self.descricao_atividadeEdit.get()
            periodo_estudoEdit = self.periodo_estudoEdit.get()
            fk_Assunto_id = self.astSelected




            if self.atividadeCRUD.atualizar(id_atividade,nome_atividadeEdit,descricao_atividadeEdit,periodo_estudoEdit,fk_Assunto_id):
                self.atividadeList.item(self.atividadeList.focus(), values=(str(id_atividade),nome_atividadeEdit,descricao_atividadeEdit,periodo_estudoEdit))
                mb.showinfo("Mensagem", "Alteração executada com sucesso.")
                self.nome_atividadeEdit.delete(0, tk.END)
                self.descricao_atividadeEdit.delete(0, tk.END)
                self.periodo_estudoEdit.delete(0, tk.END)
                self.nome_atividadeEdit.focus_set()
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")
                self.nome_atividadeEdit.focus_set()


   
    def _on_combo_changed(self, event):
        index = self.assuntoEdit.current()
        self.astSelected = self.astResult[index][0]
        self.carregar_dados_iniciais_treeView()
        



#janela = tk.Tk()
#principal = AtividadeView(janela)
#janela.title('Cadastro de Atividade')
#janela.geometry("800x340+0+0")
#janela.configure(background="#7FFFD4")
#janela.mainloop()