from lib.msgs import msg_erro
from nanoid import generate
from datetime import datetime


def gerar_id_pedido():
    alfabeto = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    id_transacao = generate(alfabeto, 8)
    return id_transacao

def validar_opcao(maximo = 8):
    while True:
        try:
            opcao = int(input('Escolha uma opção >> '))
            if opcao <= 0:
                msg_erro('Digite um número inteiro válido.')
                continue
            elif opcao > maximo:
                msg_erro('Opção inválida.')
                continue
            return opcao
        except ValueError:
            msg_erro('Digite um número inteiro válido (apenas números).')

def validar_nome_loja(txt):
    while True:
        nome_loja = str(input(txt)).strip().title()
        if nome_loja == '':
            msg_erro('Descrição inválida.')
        elif len(nome_loja) > 25:
            msg_erro('A descrição deve conter no máximo 25 caracteres.')
        elif nome_loja.isnumeric():
            msg_erro('A descrição não deve conter apenas números.')
        else:
            return nome_loja

def validar_nome_produto(txt):
    while True:
        nome_produto = str(input(txt)).strip().title()
        if nome_produto == '':
            msg_erro('Descrição inválida.')
        elif len(nome_produto) > 35:
            msg_erro('A descrição deve conter no máximo 35 caracteres.')
        elif nome_produto.isnumeric():
            msg_erro('A descrição não deve conter apenas números.')
        else:
            return nome_produto

def validar_valor(txt):
    while True:
        valor = input(txt).strip().replace(',', '.')
        try:
            valor = float(valor)
            if valor <= 0:
                msg_erro('O valor da transação deve ser maior que zero.')
            else:
                return valor
        except ValueError:
            msg_erro('Digite um valor numérico válido.')

def validar_data(txt):
    while True:
        data_texto = input(txt).strip()
        try:
            formato_de_data = datetime.strptime(data_texto, "%d/%m/%Y").date()
            hoje = datetime.today().date()
            if formato_de_data < hoje:
                msg_erro('A data de previsão de entrega não pode ser no passado!')
                continue
            return data_texto
        except ValueError:
            msg_erro('Data inválida ou formato incorreto! Use o formato DD/MM/AAAA (ex: 25/12/2026).')

def formatar_para_real(valor):
    valor_formatado = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado

def validar_id(msg):
    while True:
        entrada_id = input(msg).strip().upper()
        if entrada_id == '':
            msg_erro('ID inválido.')
        elif len(entrada_id) > 8 or len(entrada_id) < 8:
            msg_erro('IDs tem 8 caracteres apenas.')
        elif len(entrada_id) == 8:
            return entrada_id
