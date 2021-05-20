import os
from assunto import Assunto

class AssuntoView:

    def cadastrar(self):
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)

        assunto = Assunto()
        
        num_assuntos = int(input("Quantos registros de assuntos quer criar: "))
        for n in range(1, num_assuntos + 1):
            print("Entre com os dados do assunto # ", n)
            tema = input("Tema: ")
            descricao_assunto = input("Descriçâo: ")    
            assunto.cadastrar(tema,descricao_assunto)    
            print() 
        print("Assunto cadastrado com sucesso!!!")
