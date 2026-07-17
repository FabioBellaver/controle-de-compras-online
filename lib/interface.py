from lib.cores import cores
from lib.util import validar_opcao


def titulo_app(txt):
    texto = f'<< {txt.upper()} >>'
    print(f'{cores["cz"]}~{cores["limpa"]}' * 120)
    print(f'{cores["az"]}{texto.center(120)}{cores["limpa"]}')
    print(f'{cores["cz"]}~{cores["limpa"]}' * 120)

def titulo(txt):
    print(f'{cores["az"]}{txt.center(120).upper()}{cores["limpa"]}')
    print(f'{cores["cz"]}~{cores["limpa"]}' * 120)

def separador():
    print(f'{cores["cz"]}~{cores["limpa"]}' * 120)



def menu():
    titulo('Menu')
    opcoes_menu = [
        'Adicionar pedido', # 1
        'Atualizar status do pedido', # 2
        'Listar todos os pedidos', # 3
        'Listar pedidos a caminho', # 4
        'Buscar pedido (por loja ou produto)', # 5
        'Relatório de gastos por loja', # 6
        'Remover pedido', # 7
        'Sair', # 8
    ]
    for item, opcao in enumerate(opcoes_menu):
        print(f'{cores["negrito"]}{cores["ci"]}[ {item + 1} ]{cores["limpa"]} {opcao}')