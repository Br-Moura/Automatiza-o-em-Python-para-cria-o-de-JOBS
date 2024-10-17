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

def extrair_caminho_arquivo(caminho_arquivo):
    # Abre o arquivo PRD e lê seu conteúdo
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = file.read()

    # Ajuste para lidar com o caractere '_' corretamente na expressão regular
    # Agora, o caractere '_' será tratado como parte do caminho, não como um caractere especial
    # O padrão vai capturar desde "PAYMENT" até o nome do arquivo com extensão .PRD
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

pasta_inicial = 'C:/Users/mourabre/Desktop/criarjob/PRD' # Caminho inicial para a pasta onde o arquivo será salvo (modifique para sua pasta específica)

caminho_arquivo = selecionar_arquivo(pasta_inicial) # Chama a função para abrir a janela de diálogo e selecionar o arquivo

if caminho_arquivo: # Verifica se o arquivo foi selecionado
    # Exibe o caminho do arquivo selecionado
    print(f"Arquivo selecionado: {caminho_arquivo}")

    # Extrai o caminho do arquivo
    caminho_extraido = extrair_caminho_arquivo(caminho_arquivo)

    # Exibe o caminho extraído (apenas o caminho, sem fragmentos indesejados)
    print(f"Caminho extraído do arquivo: {caminho_extraido}")

    # Agora você pode abrir o arquivo como desejar
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = file.readlines()
        # Defina o padrão para o registro (14 dígitos)
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
else:
    print("Nenhum arquivo foi selecionado.")
    
# Entrada dos dados pelo usuário
section = input("Digite o nome da seção (ex: SV02062300005080101): ")
customer = input("Digite o cliente: ")
machineid = input("Digite o machineid: ")
machinetype = input("Digite o machinetype: ")
parentjobid = input("Digite o parentjobid: ")
pieces = input("Digite o número de peças: ")
processid = input("Digite o processid: ")
prodfile = input("Digite o prodfile: ")
prodtype = input("Digite o prodtype: ")
pulist = "1-E"
status = ""


directory = "C:/Users/mourabre/Desktop/criarjob/INI" # Caminho do diretório onde o .ini será salvo

# Criar o arquivo .ini com os dados fornecidos
create_ini_file(section, customer, machineid, machinetype, parentjobid, pieces, processid, prodfile, prodtype, pulist, status, directory)

