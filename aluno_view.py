import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from typing import ItemsView

from aluno import Aluno

class Aluno_View:

    def __init__(self,win):
         self.aluno_viewCRUD = Aluno() 

         

         self.id_alunoLabel = tk.Label(win, text='Id')
         self.id_alunoEdit = tk.Entry(width=10, bd=3) 

         self.matriculaLabel = tk.Label(win, text='Matricula')
         self.matriculaEdit = tk.Entry(width=10, bd=3) 

         self.nomeLabel = tk.Label(win, text='Nome')
         self.nomeEdit = tk.Entry(width=32, bd=3) 

         self.maeLabel = tk.Label(win, text='Nome da Mae')
         self.maeEdit = tk.Entry(width=32, bd=3) 

         self.paiLabel = tk.Label(win, text='Nome do Pai')
         self.paiEdit = tk.Entry(width=32, bd=3) 

         self.data_nascimentoLabel = tk.Label(win, text='Data Nascimento')
         self.data_nascimentoEdit = tk.Entry(width=10, bd=3) 

         self.telefoneLabel = tk.Label(win, text='Telefone')
         self.telefoneEdit = tk.Entry(width=10, bd=3) 

         self.cepLabel = tk.Label(win, text='Cep')
         self.cepEdit = tk.Entry(width=10, bd=3) 
       
         self.emailLabel = tk.Label(win, text='email')
         self.emailEdit = tk.Entry(width=32, bd=3) 

         
         self.instituição_de_ensino = ttk.Treeview(win, columns=(1,2), show='headings')

         self.verscrlbar = ttk.Scrollbar(win,orient="vertical", command=self.instituição_de_ensino.yview)
         self.verscrlbar.pack(side = 'right', fill='x')
         self.instituição_de_ensino.configure(yscrollcommand = self.verscrlbar.set)
         self.instituição_de_ensino.heading(1, text='ID')
         self.instituição_de_ensino.heading(2, text='Nome')
         self.instituição_de_ensino.column(1, minwidth=0, width=60)
         self.instituição_de_ensino.column(2, minwidth=0, width=320)
         self.instituição_de_ensino.pack()
         self.instituição_de_ensino.bind("<<TreeviewSelect>>", self._on_inserir)
         

              

         self.btnCadastrar = tk.Button (win,text='Inserir', width=12, command=self._on_inserir)


         #criar tamanho e posição

         self.id_alunoLabel.place(x=10,y=10)
         self.id_alunoEdit.place (x=95, y=10)

         self.matriculaLabel.place(x=170,y=10)
         self.matriculaEdit.place (x=228, y=10)

         self.nomeLabel.place(x=10,y=60)
         self.nomeEdit.place (x=95, y=60)

         self.emailLabel.place(x=10,y=85)
         self.emailEdit.place (x=95, y=85)

         self.telefoneLabel.place(x=10,y=110)
         self.telefoneEdit.place (x=95, y=110)

         self.cepLabel.place(x=195,y=110)
         self.cepEdit.place (x=228, y=110)

         self.data_nascimentoLabel.place(x=10,y=35)
         self.data_nascimentoEdit.place (x=228, y=35)

         self.paiLabel.place(x=10,y=135)
         self.paiEdit.place (x=95, y=135)

         self.maeLabel.place(x=10,y=160)
         self.maeEdit.place (x=95, y=160)

         self.btnCadastrar.place(x=300, y=85)
         
         self.instituição_de_ensino.place(x=10, y=190)
         self.verscrlbar.place(x=375, y=218, height=195)
         
    def _on_inserir(self):
        nome = self.nomeEdit.get()
        
        if  self.aluno_viewCRUD.cadastrar(nome):

            id = self.aluno_viewCRUD.consultar_ultimo_id()
            #numeroLinhas = len(self.departamentoList.get_children())
            self.aluno_viewCRUD.insert('','end',iid=(id+1),values=(str(id),nome))
    
            mb.showinfo("Mensagem", "Cadastro executado com sucesso.")       
            self.nomeEdit.delete(0, tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no cadastro.") 
            self.nomeEdit.focus_set()


#janela = tk.Tk()
#principal = Aluno_View(janela)
#janela.title("Cadastro de Alunos")
#janela.geometry ("400x450+0+0")
#janela.configure(background="#7FFFD4")
#janela.mainloop()