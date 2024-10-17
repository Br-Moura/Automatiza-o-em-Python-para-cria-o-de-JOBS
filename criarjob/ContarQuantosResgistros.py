import re
import os
import tkinter as tk
from tkinter import filedialog


def selecionar_arquivo(pasta_inicial):
    # Cria uma janela oculta
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Abre uma janela de diálogo para selecionar o arquivo na pasta inicial
    caminho_arquivo = filedialog.askopenfilename(
        initialdir=pasta_inicial,  # Define a pasta inicial
        title="Selecione o arquivo",  # Título da janela
        filetypes=[("Arquivos .prd", "*.prd"), ("Todos os arquivos", "*.*")]  # Tipos de arquivo
    )
    
    return caminho_arquivo

# Caminho inicial para a pasta desejada (modifique para sua pasta específica)
pasta_inicial = 'C:/Users/mourabre/Desktop/criarjob/PRD'

# Chama a função para abrir a janela de diálogo e selecionar o arquivo
caminho_arquivo = selecionar_arquivo(pasta_inicial)

# Exibe o caminho do arquivo selecionado
print(f"Arquivo selecionado: {caminho_arquivo}")

# Agora você pode abrir o arquivo como desejar, por exemplo:
if caminho_arquivo:
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = file.readlines()
        # Faça algo com o conteúdo do arquivo
    # Define o padrão para o registro (14 dígitos)
    pattern = r'\b\d{14}\b'

    # Encontrar todas as correspondências do padrão no conteúdo do arquivo
    matches = []
    for line in conteudo:  # Corrigido para iterar sobre as linhas do conteúdo do arquivo
        matches.extend(re.findall(pattern, line))

    # Exibe as correspondências encontradas
    print("Registros encontrados:", matches)
    
    # Conta o número de registros
    record_count = len(matches)

    # Exibe a contagem de registros
    print(f"Número de registros encontrados: {record_count}")

