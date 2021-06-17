import os
from collections import OrderedDict
from conexao import Conexao

from aluno import Aluno
from aluno_view import Aluno_View



def limpa_tela():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)

def menu():  
    limpa_tela()

    options = OrderedDict(
    {
        '1': 'Criar Tabelas',
        '2': 'Cadastrar Aluno',
        '3': 'Sair'
    })

    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print()
    
    escolha = input('Escolha uma opção: ').upper()
    if escolha == '1':
        conn = Conexao()
        conn.createTables()
    else:
        if escolha == '2':
            telaCadastroAssunto = Aluno_View()
            telaCadastroAssunto.cadastrar()
        else:
            if escolha == '3':
                return False
            
    limpa_tela()
    return True

def main():
    sair = True
    while(sair):
        sair = menu()

main()