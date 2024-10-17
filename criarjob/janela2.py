import os
import re
import tkinter as tk
from tkinter import filedialog

####### Funções ##############

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

def extrair_nome_arquivo(caminho_arquivo):
    # Abre o arquivo PRD e lê seu conteúdo
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = file.read()

    # Ajuste para lidar com o caractere '_' corretamente na expressão regular
    match = re.search(r'(PAYMENT\\(?:[A-Z0-9_]+\\)*\d{2}-\d{2}\\[A-Z0-9_]+)(?=\.PRD)', conteudo)
    
    if match:
        caminho_final = match.group(1)
        nome_arquivo = os.path.basename(caminho_final)  # Extrai apenas o nome do arquivo
        return nome_arquivo
    else:
        return "Nome do arquivo não encontrado."

def extrair_caminho_arquivo(caminho_arquivo):
    # Abre o arquivo PRD e lê seu conteúdo
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = file.read()

    # Ajuste para lidar com o caractere '_' corretamente na expressão regular
    # Agora, o caractere '_' será tratado como parte do caminho, não como um caractere especial
    match = re.search(r'(PAYMENT\\(?:[A-Z0-9_]+\\)*\d{2}-\d{2}\\[A-Z0-9_]+\.PRD)', conteudo)

    if match:
        # Se encontrou, retorne o caminho
        caminho_final = match.group(1)
        return caminho_final
    else:
        return "Caminho não encontrado."

def create_ini_file(section, customer, machineid, machinetype, parentjobid, pieces, processid, prodfile, prodtype, pulist, status, directory):
    # Caminho completo para o arquivo .ini
    filename = os.path.join(directory, f'{section}.ini')

    # Conteúdo do arquivo .ini
    ini_content = f"""[{section}]
customer={customer}
machineid={machineid}
machinetype={machinetype}
parentjobid={parentjobid}
pieces={pieces}
processid={processid}
prodfile={prodfile}
prodtype={prodtype}
pulist={pulist}
status={status}
"""

    try:
        # Verificar se o diretório existe e criar se não existir
        if not os.path.exists(directory):
            print(f"A pasta '{directory}' não existe. Criando...")
            os.makedirs(directory)

        # Escrever o conteúdo no arquivo .ini
        with open(filename, 'w') as file:
            file.write(ini_content)
        
        print(f"Arquivo '{filename}' criado com sucesso!")

    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")

####### Funções ##############

pasta_inicial = 'C:/Users/mourabre/Desktop/criarjob/PRD'  # Caminho inicial para a pasta onde o arquivo será salvo

# Chama a função para abrir a janela de diálogo e selecionar o arquivo
caminho_arquivo = selecionar_arquivo(pasta_inicial)

if caminho_arquivo:  # Verifica se o arquivo foi selecionado
    print(f"Arquivo selecionado: {caminho_arquivo}")

    # Extrai o caminho completo do arquivo
    caminho_extraido = extrair_caminho_arquivo(caminho_arquivo)
    print(f"Caminho extraído do arquivo: {caminho_extraido}")  # Exibe o caminho extraído

    # Extrai o nome do arquivo sem a extensão
    nome_arquivo_extraido = extrair_nome_arquivo(caminho_arquivo)
    print(f"Nome do arquivo extraído: {nome_arquivo_extraido}")  # Exibe o nome do arquivo extraído (sem caminho e sem extensão)

    # Abrir e ler o conteúdo do arquivo
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = file.readlines()
        pattern = r'\b\d{14}\b'  # Defina o padrão para o registro (14 dígitos)

        matches = []  # Encontrar todas as correspondências do padrão no conteúdo do arquivo
        for line in conteudo:
            matches.extend(re.findall(pattern, line))
        
        print("Registros encontrados:", matches)  # Exibe as correspondências encontradas
        Registros = len(matches)  # Conta o número de registros
        print(f"Número de registros encontrados: {Registros}")  # Exibe a contagem de registros
else:
    print("Nenhum arquivo foi selecionado.")

# Entrada dos dados pelo usuário
section = nome_arquivo_extraido
customer = "PyautoUPP"
machineid = ""
machinetype = ""
parentjobid = ""
pieces = Registros
processid = ""
prodfile = nome_arquivo_extraido  # Usando o nome do arquivo extraído
prodtype = "4"
pulist = "1-E"
status = ""

# Caminho do diretório onde o arquivo será salvo
directory = "C:/Users/mourabre/Desktop/criarjob/INI"

# Criar o arquivo .ini com os dados fornecidos
create_ini_file(section, customer, machineid, machinetype, parentjobid, pieces, processid, prodfile, prodtype, pulist, status, directory)
