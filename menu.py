import tkinter as tk 
import os 
from aluno_view import Aluno_View 
from assunto_view2 import AssuntoView 
from atividade_view import AtividadeView  
from conexao import Conexao 
 

class Menu: 
    def __init__(self, window): 
       self.window = window 

       menu = tk.Menu(window) 

       cadastroMenu = tk.Menu(menu, tearoff = False) 
       cadastroMenu.add_command(label = "Aluno", command=self._open_aluno) 
       cadastroMenu.add_command(label = "Assunto", command=self._open_assunto) 
       cadastroMenu.add_command(label = "Atividade", command=self._open_atividade) 
       cadastroMenu.add_command(label = "Sair", command=window.destroy) 
       menu.add_cascade(menu = cadastroMenu, label = "Cadastros") 


       atividadeMenu = tk.Menu(menu, tearoff = False) 
       atividadeMenu.add_command(label = "Aluno", command=self._open_aluno) 
       atividadeMenu.add_command(label = "Assunto", command=self._open_assunto) 
       menu.add_cascade(menu = atividadeMenu, label = "Atividade") 
   
       bancoMenu = tk.Menu(menu, tearoff = False) 
       bancoMenu.add_command(label = "Criar", command=self._criar_banco) 
       menu.add_cascade(menu = bancoMenu, label = "Banco") 
      
       window.config(menu=menu) 

  
    def _open_aluno(self): 
        janela=tk.Toplevel(self.window) 
        janela.title('Cadastro de Alunos') 
        janela.geometry("400x450+0+0") 
        janela.configure(background="#7FFFD4")
        principal=Aluno_View(janela)
        janela.mainloop() 

  

    def _open_assunto(self): 
        janela=tk.Toplevel(self.window) 
        janela.title('Cadastro de Assuntos') 
        janela.geometry( "950x400+0+0") 
        janela.configure(background="#7FFFD4")
        principal=AssuntoView(janela) 
        janela.mainloop() 

  

    def _open_atividade(self): 
        janela=tk.Toplevel(self.window) 
        janela.title('Cadastro de Atividades') 
        janela.geometry("800x340+0+0") 
        janela.configure(background="#7FFFD4")
        principal=AtividadeView(janela) 
        janela.mainloop() 

  

    def _criar_banco(self): 
        file = 'instituição_de_ensino.db' 
        location = os.path.dirname(os.path.abspath(" instituição_de_ensino.db")) 
        path = os.path.join(location, file) 
        os.remove(path) 

        conn = Conexao() 
        conn.createTables()
