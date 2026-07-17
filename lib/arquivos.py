import json
import os

def criar_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=4, ensure_ascii=False)

def ler_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        criar_arquivo(nome_arquivo)
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

def salvar_arquivo(nome_arquivo, dados):
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)