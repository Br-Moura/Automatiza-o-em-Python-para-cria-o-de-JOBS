import os
import re
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

def extrair_caminho_arquivo(caminho_arquivo):
    # Abre o arquivo PRD e lê seu conteúdo
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = file.read()

    # Buscar pela palavra "PAYMENT\" e garantir que extraímos todo o caminho a partir de "PAYMENT"
    match = re.search(r'(PAYMENT\\(?:[A-Z0-9]+\\)*\d{2}-\d{2}\\[A-Z0-9]+\.PRD)', conteudo)

    if match:
        # Se encontrou, retorne o caminho
        caminho_final = match.group(1)
        return caminho_final
    else:
        return "Caminho não encontrado."

# Caminho inicial para a pasta onde o arquivo será salvo (modifique para sua pasta específica)
pasta_inicial = 'C:/Users/mourabre/Desktop/criarjob/PRD'

# Chama a função para abrir a janela de diálogo e selecionar o arquivo
caminho_arquivo = selecionar_arquivo(pasta_inicial)

# Verifica se o arquivo foi selecionado
if caminho_arquivo:
    # Exibe o caminho do arquivo selecionado
    print(f"Arquivo selecionado: {caminho_arquivo}")

    # Extrai o caminho do arquivo
    caminho_extraido = extrair_caminho_arquivo(caminho_arquivo)

    # Exibe o caminho extraído (apenas o caminho, sem fragmentos indesejados)
    print(f"Caminho extraído do arquivo: {caminho_extraido}")
else:
    print("Nenhum arquivo foi selecionado.")
