import sqlite3
#import psycopg2
class Conexao:

    def conectar(self):
        conexao = None
        db_path = 'instituição_de_ensino.db'
        try:
            conexao = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
            #conexao = sqlite3.connect(db_path)
        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")
        return conexao

        #conexao = None
        #try:
        #  conexao = psycopg2.connect(user="postgres",
        #                          password="t1fas777",
        #                          host="127.0.0.1",
        #                          port="5432",
        #                          database="postgres")
        #except (Exception, psycopg2.Error) as error :
        #    print(f"Erro ao conectar o banco de dados.")
        #return conexao

    def createTableAssunto(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Assunto (id_assunto INTEGER PRIMARY KEY AUTOINCREMENT,tema varchar NOT NULL, descricao_assunto varchar NOT NULL);'
        cursor.execute(sql)
        conexao.commit()

    def createTableAnalisa(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Analisa (fk_assunto_id int, fk_atividade_id int, FOREIGN KEY (fk_assunto_id) REFERENCES Assunto (id_assunto),FOREIGN KEY (fk_atividade_id) REFERENCES Atividade  (id_atividade));'
        cursor.execute(sql)
        conexao.commit()

    def createTableAtividade(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Atividade (id_atividade INTEGER PRIMARY KEY AUTOINCREMENT,periodo_estudo DATE NOT NULL,descricao_atividade varchar NOT NULL);'
        cursor.execute(sql)
        conexao.commit()

    def createTableStatus_atividade(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Status_atividade (fk_atividade_id int, fk_aluno_id int, analise CHAR(1) NOT NULL,conclusao CHAR(1) NOT NULL,FOREIGN KEY (fk_atividade_id) REFERENCES Atividade (id_atividade), FOREIGN KEY (fk_aluno_id) REFERENCES Aluno  (id_aluno));'
        cursor.execute(sql)
        conexao.commit()

    def createTableAluno(self,conexao,cursor):
        sql = 'CREATE TABLE IF NOT EXISTS Aluno (id_aluno INTEGER PRIMARY KEY AUTOINCREMENT, matricula VARCHAR(12) NOT NULL UNIQUE,nome VARCHAR NOT NULL,mae VARCHAR NOT NULL,pai VARCHAR NOT NULL,data_nascimento DATE NOT NULL,telefone VARCHAR(11) NOT NULL,cep VARCHAR(8) NOT NULL,email VARCHAR NOT NULL);'
        cursor.execute(sql) 
        conexao.commit()

    def createTables(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        self.createTableAssunto(conexao,cursor)
        self.createTableAnalisa(conexao,cursor)
        self.createTableAtividade(conexao,cursor)
        self.createTableStatus_atividade(conexao,cursor)
        self.createTableAluno(conexao,cursor)
