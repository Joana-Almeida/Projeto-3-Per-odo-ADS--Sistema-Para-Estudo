import sqlite3
from sqlite3.dbapi2 import IntegrityError
from conexao import Conexao


class Atividade:

    def cadastrar(self,nome_atividade,descricao_atividade,periodo_estudo,fk_Assunto_id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO atividade (nome_atividade,descricao_atividade,periodo_estudo,fk_Assunto_id) VALUES (?,?,?,?)'
            cursor.execute(sql,(nome_atividade,descricao_atividade,periodo_estudo,fk_Assunto_id))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de atividades: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM atividade').fetchall()
        except IntegrityError as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset


    def consultar_detalhes(self, id_atividade):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = 'SELECT * FROM atividade WHERE id = ?'

        try:
            resultset =  cursor.execute(sql,[id_atividade]).fetchall()
        except IntegrityError as e:
            print(f"O erro '{e}' ocorreu.")


        cursor.close()
        conexao.close()
        return resultset


    def consultar_ultimo_id(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset = cursor.execute('SELECT MAX(id) FROM atividade').fetchone()
        except IntegrityError as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]


    def atualizar(self,id_atividade,nome_atividade,descricao_atividade,periodo_estudo,fk_Assunto_id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE atividade SET nome_atividade = ?, descricao_atividade = ?, periodo_estudo = ?, fk_Assunto_id = ? WHERE id = (?)'
            cursor.execute(sql,(nome_atividade,descricao_atividade,periodo_estudo,fk_Assunto_id,id_atividade))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de empregados: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def consultar_por_assunto(self,ast):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT e.id, e.nome_atividade, e.descricao_atividade, e.periodo_estudo, e.fk_Assunto_id 
                FROM atividade as e 
                WHERE fk_Assunto_id = ?"""

        
        try:
            resultset =  cursor.execute(sql,(ast,)).fetchall()
        except IntegrityError as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset
