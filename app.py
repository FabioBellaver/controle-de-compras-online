from time import sleep

from lib.arquivos import criar_arquivo, ler_arquivo
from lib.dados import adicionar_pedido
from lib.interface import titulo_app, menu, separador, titulo, interface_adicionar_pedido, listar_pedidos, \
    interface_atualizar_status_pedido, listar_pedidos_a_caminho, buscar_pedido, gastos_por_loja, \
    interface_remover_pedido
from lib.uteis import validar_opcao


titulo_app('controle de compras online')
nome_arquivo = 'pedidos.json'
criar_arquivo(nome_arquivo)
ler_arquivo(nome_arquivo)
while True:
    sleep(0.4)
    menu()
    separador()
    opcao = validar_opcao()
    separador()
    if opcao == 1:
        titulo('Adicionar pedido')
        dados = interface_adicionar_pedido()
        adicionar_pedido(nome_arquivo, dados)
    elif opcao == 2:
        titulo('Atualizar status do pedido')
        interface_atualizar_status_pedido(nome_arquivo)
    elif opcao == 3:
        titulo('Listar todos os pedidos')
        listar_pedidos(nome_arquivo)
    elif opcao == 4:
        titulo('Listar pedidos a caminho')
        listar_pedidos_a_caminho(nome_arquivo)
    elif opcao == 5:
        titulo('Buscar pedido (por loja ou produto)')
        buscar_pedido(nome_arquivo)
    elif opcao == 6:
        titulo('Relatório de gastos por loja')
        gastos_por_loja(nome_arquivo)
    elif opcao == 7:
        titulo('Remover pedido')
        interface_remover_pedido(nome_arquivo)
    elif opcao == 8:
        break
titulo_app('sistema encerrado')
