from lib.msgs import msg_erro


def validar_opcao():
    while True:
        try:
            opcao = int(input('Escolha uma opção >> '))
            if opcao <= 0:
                msg_erro('Digite um número inteiro válido.')
                continue
            elif opcao > 8:
                msg_erro('Opção inválida.')
                continue
            return opcao
        except ValueError:
            msg_erro('Digite um número inteiro válido (apenas números).')