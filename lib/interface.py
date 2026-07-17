from datetime import datetime

from lib.arquivos import ler_arquivo
from lib.cores import cores
from lib.dados import dados_de_pedidos, atualizar_status, remover_pedido
from lib.msgs import msg_sucesso, msg_alerta, msg_erro
from lib.uteis import validar_nome_loja, validar_nome_produto, validar_valor, validar_data, \
    gerar_id_pedido, formatar_para_real, validar_id, validar_opcao, validar_termo_de_busca


def titulo_app(txt):
    texto = f'<< {txt.upper()} >>'
    print(f'{cores["cz"]}~{cores["limpa"]}' * 130)
    print(f'{cores["az"]}{texto.center(120)}{cores["limpa"]}')
    print(f'{cores["cz"]}~{cores["limpa"]}' * 130)

def titulo(txt):
    print(f'{cores["az"]}{txt.center(130).upper()}{cores["limpa"]}')
    print(f'{cores["cz"]}~{cores["limpa"]}' * 130)

def separador():
    print(f'{cores["cz"]}~{cores["limpa"]}' * 130)

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

def interface_adicionar_pedido():
    id_pedido = gerar_id_pedido()
    loja = validar_nome_loja('Digite o nome da loja: ').upper()
    produto = validar_nome_produto('Digite o nome do produto: ').upper()
    status = 'COMPRADO'
    data_compra = datetime.today().strftime('%d/%m/%Y')
    valor = validar_valor('Digite o valor do produto: ')
    previsao_entrega = validar_data('Digite a data de previsão de entrega [DD/MM/AAAA]: ')
    pedido = {
        'id_pedido': id_pedido,
        'loja': loja,
        'produto': produto,
        'status': status,
        'valor': valor,
        'data_compra': data_compra,
        'previsao_entrega': previsao_entrega,
    }
    separador()
    msg_sucesso(f'ID "{id_pedido}", loja "{loja}", produto "{produto}", valor "{valor}", previsão "{previsao_entrega}". Pedido adicionado.')
    separador()
    return pedido

def menu_status(id_pedido):
    titulo(f'Alterar status do pedido: {id_pedido}')
    opcoes_status = ['COMPRADO', 'ENVIADO', 'ENTREGUE', 'CANCELADO']
    for item, opcao in enumerate(opcoes_status):
        print(f'{cores["negrito"]}{cores["ci"]}[ {item + 1} ]{cores["limpa"]} {opcao}')

def interface_atualizar_status_pedido(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    pedido_encontrado = False
    if dados:
        entrada_id = validar_id('Digite o ID para atualizar: ')
        for dado in dados:
            if dado['id_pedido'] == entrada_id:
                msg_sucesso(f'Pedido "{dado["id_pedido"]}" encontrado. Status atual: {dado["status"]}')
                pedido_encontrado = True
                break
        if pedido_encontrado:
            menu_status(entrada_id)
            separador()
            opcao = validar_opcao(4)
            separador()
            status = ['COMPRADO', 'ENVIADO', 'ENTREGUE', 'CANCELADO']
            status_escolhido = status[opcao - 1]
            atualizar_status(nome_arquivo, entrada_id, status_escolhido)
            msg_sucesso(f'Pedido {dado["id_pedido"]} ({dado["produto"]}) atualizado.')
        else:
            msg_erro(f'O ID "{entrada_id}" não existe.')
    else:
        msg_alerta('Não existem pedidos cadastrados.')

def cabecalho_lista():
    print(f'{cores["negrito"]}{"ID":<10}', end ='')
    print(f'{"LOJA":<25}', end ='')
    print(f'{"PRODUTO":<35}', end ='')
    print(f'{"STATUS":<12}', end ='')
    print(f'{"VALOR":<12}', end ='')
    print(f'{"DATA COMPRA":<15}', end ='')
    print(f'{"PREV ENTREGA":<15}{cores["limpa"]}')
    separador()

def listar_pedidos(nome_arquivo):
    status = ['COMPRADO', 'ENVIADO', 'ENTREGUE', 'CANCELADO']
    dados = ler_arquivo(nome_arquivo)
    if dados:
        cabecalho_lista()
        for dado in dados:
            comprado = dado["status"] == status[0]
            enviado = dado["status"] == status[1]
            entregue = dado["status"] == status[2]
            cancelado = dado["status"] == status[3]
            print(f'{cores["negrito"]}{dado["id_pedido"]:<10}{cores["limpa"]}', end='')
            print(f'{dado["loja"]:<25}', end='')
            print(f'{dado["produto"]:<35}', end='')
            if comprado or enviado:
                print(f'{cores["am"]}{dado["status"]:<12}{cores["limpa"]}', end='')
            if entregue:
                print(f'{cores["vd"]}{dado["status"]:<12}{cores["limpa"]}', end='')
            if cancelado:
                print(f'{cores["vm"]}{dado["status"]:<12}{cores["limpa"]}', end='')
            print(f'{formatar_para_real(dado["valor"]):<12}', end='')
            print(f'{dado["data_compra"]:<15}', end='')
            print(f'{dado["previsao_entrega"]:<15}')
        separador()
        estatisticas = dados_de_pedidos(nome_arquivo)
        rodape_dados = (f'{cores["negrito"]}Quantidade de pedidos: {cores["limpa"]}{estatisticas["qtd_pedidos"]} | '
                        f'{cores["negrito"]}Valor total: {cores["limpa"]}{formatar_para_real(estatisticas["valor_total"])}')
        print(f'{rodape_dados.center(130)}')
        separador()
    else:
        msg_alerta("Não existem pedidos cadastrados.")
        separador()

def listar_pedidos_a_caminho(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    qtd_pedidos = 0
    valor_total = 0
    if dados:
        pedido_encontrado = False
        cabecalho_lista()
        for dado in dados:
            if dado['status'] == 'ENVIADO':
                pedido_encontrado = True
                qtd_pedidos += 1
                valor_total += dado['valor']
                print(f'{cores["negrito"]}{dado["id_pedido"]:<10}{cores["limpa"]}', end='')
                print(f'{dado["loja"]:<25}', end='')
                print(f'{dado["produto"]:<35}', end='')
                print(f'{cores["am"]}{dado["status"]:<12}{cores["limpa"]}', end='')
                print(f'{formatar_para_real(dado["valor"]):<12}', end='')
                print(f'{dado["data_compra"]:<15}', end='')
                print(f'{dado["previsao_entrega"]:<15}')
        if not pedido_encontrado:
            msg_alerta('Não existem pedidos a caminho.')
        separador()
        rodape_dados = (f'{cores["negrito"]}Quantidade de pedidos: {cores["limpa"]}{qtd_pedidos} | '
                        f'{cores["negrito"]}Valor total: {cores["limpa"]}{formatar_para_real(valor_total)}')
        print(f'{rodape_dados.center(130)}')
        separador()
    else:
        msg_alerta('Não existem pedidos cadastrados.')

def buscar_pedido(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    qtd_pedidos = 0
    valor_total = 0
    pedido_encontrado = False
    if dados:
        termo = validar_termo_de_busca('Digite o nome da loja ou produto para encontrar pedidos: ')
        for dado in dados:
            if termo.upper() in dado['loja'].upper() or termo.upper() in dado['produto'].upper():
                pedido_encontrado = True
                break
        if pedido_encontrado:
            msg_sucesso('Pedido encontrado!')
            cabecalho_lista()
            for dado in dados:
                if termo.upper() in dado['loja'].upper() or termo.upper() in dado['produto'].upper():
                    qtd_pedidos += 1
                    valor_total += dado['valor']
                    print(f'{cores["negrito"]}{dado["id_pedido"]:<10}{cores["limpa"]}', end='')
                    print(f'{dado["loja"]:<25}', end='')
                    print(f'{dado["produto"]:<35}', end='')
                    print(f'{cores["am"]}{dado["status"]:<12}{cores["limpa"]}', end='')
                    print(f'{formatar_para_real(dado["valor"]):<12}', end='')
                    print(f'{dado["data_compra"]:<15}', end='')
                    print(f'{dado["previsao_entrega"]:<15}')
            separador()
            rodape_dados = (f'{cores["negrito"]}Quantidade de pedidos: {cores["limpa"]}{qtd_pedidos} | '
                            f'{cores["negrito"]}Valor total: {cores["limpa"]}{formatar_para_real(valor_total)}')
            print(f'{rodape_dados.center(130)}')
            separador()
        else:
            msg_erro('Termo não encontrado.')
    else:
        msg_alerta('Não existem pedidos cadastrados.')

def gastos_por_loja(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    if dados:
        totais_por_loja = {}
        for dado in dados:
            if dado['status'] != 'CANCELADO':
                nome_loja = dado['loja']
                valor_pedido = dado['valor']
                if nome_loja not in totais_por_loja:
                        totais_por_loja[nome_loja] = 0
                totais_por_loja[nome_loja] += valor_pedido
        print(f'{"LOJA":<30} | {"TOTAL GASTO":<15}')
        separador()
        for loja, total in totais_por_loja.items():
            print(f'{loja:<30} | {formatar_para_real(total):<15}')
        separador()
    else:
        msg_alerta('Não existem pedidos cadastrados.')

def interface_remover_pedido(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    if dados:
        id_pedido = validar_id('Digite o id do pedido: ')
        id_encontrado = False
        for dado in dados:
            if dado['id_pedido'] == id_pedido:
                id_encontrado = True
                break
        if id_encontrado:
            remover_pedido(nome_arquivo, id_pedido)
            msg_sucesso(f'Pedido "{dado["id_pedido"]}" ({dado["produto"]}, {dado["loja"]}) removido!')
        else:
            msg_erro(f'O pedido com ID {id_pedido} não foi encontrado.')
    else:
        msg_alerta('Não existem pedidos cadastrados.')
