from lib.arquivos import ler_arquivo, salvar_arquivo


def adicionar_pedido(nome_arquivo, pedido):
    dados = ler_arquivo(nome_arquivo)
    dados.append(pedido)
    salvar_arquivo(nome_arquivo, dados)

def atualizar_status(nome_arquivo, id_pedido, novo_status):
    dados = ler_arquivo(nome_arquivo)
    for pedido in dados:
        if pedido['id_pedido'] == id_pedido:
            pedido['status'] = novo_status
            break
    salvar_arquivo(nome_arquivo, dados)

def dados_de_pedidos(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    valor_total = 0
    for dado in dados:
        if dado['valor']:
            valor_total += dado['valor']
    dados_pedidos = {
        'qtd_pedidos': len(dados),
        'valor_total': valor_total
    }
    return dados_pedidos

def remover_pedido(nome_arquivo, id_pedido):
    dados = ler_arquivo(nome_arquivo)
    lista_atualizada = []
    for dado in dados:
        if dado['id_pedido'] != id_pedido:
            lista_atualizada.append(dado)
    salvar_arquivo(nome_arquivo, lista_atualizada)
