# coding=utf-8
# USO: cat <arquivo_de_logs> | python3 verificarLog.py 
# OU: python3 verificarLog.py <arquivo_de_log>

#%%
# Importar bibliotecas
import fileinput # acesso ao arquivo de logs via stdin ou argumentos
import json # ler arquivo de códigos de países
#%%

# Dicionário para receber os dados
registros = {}

# Lista para verificar registros duplicados
vistos = []

# Ler arquivo de códigos de países
with open('codigos.json', 'r') as arquivo:
    codigos = json.load(arquivo)

# Iterar por cada linha do log
for linha in fileinput.input():
    # Verifica se registro já foi visto
    if linha.split()[0] not in vistos:
        # Adiciona registro à lista de vistos
        vistos.append(linha.split()[0])
        # Seleciona o país de acordo com os dois primeiros dígitos
        pais = codigos[linha[:2]] 
        # Verifica se usuário está ativo
        ativo = 1 if linha.split()[1] == 'assinado' else 0
        # Preenche dicionário com dados do registro
        if pais in registros:
            registros[pais][0] += 1
            registros[pais][1] += ativo
        # Cria nova entrada para o país, caso seja o primeiro registro do país
        else:
            registros[pais] = [1, ativo]
print(registros)
with open('resultado.txt', 'w') as arquivo:
    for pais in registros.keys():
        arquivo.write(f"{pais},{registros[pais][0]},{registros[pais][1]}\n")