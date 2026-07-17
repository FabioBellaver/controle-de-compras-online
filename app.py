from lib.arquivos import criar_arquivo, ler_arquivo
from lib.dados import adicionar_pedido
from lib.interface import titulo_app, menu, separador, titulo, interface_adicionar_pedido, listar_pedidos, \
    interface_atualizar_status_pedido, listar_pedidos_a_caminho
from lib.uteis import validar_opcao

titulo_app('controle de compras online')
nome_arquivo = 'pedidos.json'
criar_arquivo(nome_arquivo)
ler_arquivo(nome_arquivo)
while True:
    menu()
    separador()
    opcao = validar_opcao()
    separador()
    if opcao == 1: # 1 - Adicionar pedido
        titulo('Adicionar pedido')
        dados = interface_adicionar_pedido()
        adicionar_pedido(nome_arquivo, dados)
    elif opcao == 2: # 2 - Atualizar status do pedido
        titulo('Atualizar status do pedido')
        interface_atualizar_status_pedido(nome_arquivo)
    elif opcao == 3: # 3 - Listar todos os pedidos
        titulo('Listar todos os pedidos')
        listar_pedidos(nome_arquivo)
    elif opcao == 4: # 4 - Listar pedidos a caminho
        titulo('Listar pedidos a caminho')
        listar_pedidos_a_caminho(nome_arquivo)
    elif opcao == 5: # 5 - Buscar pedido (por loja ou produto)
        titulo('Buscar pedido (por loja ou produto)')
    elif opcao == 6: # 6 - Relatório de gastos por loja
        titulo('Relatório de gastos por loja')
    elif opcao == 7: # 7 - Remover pedido
        titulo('Remover pedido')
    elif opcao == 8: # 8 - Sair
        break
titulo_app('sistema encerrado')
