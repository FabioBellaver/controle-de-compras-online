from lib.interface import titulo_app, menu, separador, titulo
from lib.util import validar_opcao

titulo_app('controle de compras online')

# 1 - Adicionar pedido
# 2 - Atualizar status do pedido
# 3 - Listar todos os pedidos
# 4 - Listar pedidos a caminho
# 5 - Buscar pedido (por loja ou produto)
# 6 - Relatório de gastos por loja
# 7 - Remover pedido
# 8 - Sair

while True:
    menu()
    separador()
    opcao = validar_opcao()
    separador()
    if opcao == 1: # 1 - Adicionar pedido
        titulo('Adicionar pedido')
    elif opcao == 2: # 2 - Atualizar status do pedido
        titulo('Atualizar status do pedido')
    elif opcao == 3: # 3 - Listar todos os pedidos
        titulo('Listar todos os pedidos')
    elif opcao == 4: # 4 - Listar pedidos a caminho
        titulo('Listar pedidos a caminho')
    elif opcao == 5: # 5 - Buscar pedido (por loja ou produto)
        titulo('Buscar pedido (por loja ou produto)')
    elif opcao == 6: # 6 - Relatório de gastos por loja
        titulo('Relatório de gastos por loja')
    elif opcao == 7: # 7 - Remover pedido
        titulo('Remover pedido')
    elif opcao == 8: # 8 - Sair
        break
titulo_app('sistema encerrado')
