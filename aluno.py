import sqlite3
from conexao import Conexao

class Aluno:

    def cadastrar(self,matricula,nome,mae,pai,data_nascimento,telefone,cep,email):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Aluno (matricula,nome,mae,pai,data_nascimento,telefone,cep,email) VALUES (?,?,?,?,?,?,?,?)'
            cursor.execute(sql,(matricula,nome,mae,pai,data_nascimento,telefone,cep,email))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de Aluno: {}".format(e))
            return False