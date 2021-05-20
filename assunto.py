import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Assunto:

    def cadastrar(self,tema,descricao_assunto):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Assunto (tema,descricao_assunto) VALUES (?,?)'
            cursor.execute(sql,(tema,descricao_assunto))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de assuntos: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False




    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT id_assunto,tema,descricao_assunto FROM Assunto').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset




    def excluir(self,tema,descricao_assunto):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM assunto WHERE id = (?)'
            cursor.execute(sql,[tema, descricao_assunto])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de assuntos: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False
