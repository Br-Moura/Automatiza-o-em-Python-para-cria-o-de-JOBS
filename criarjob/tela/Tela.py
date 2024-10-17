import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Combobox  # Usado para Combobox

# Função para selecionar arquivo
def selecionar_arquivo(pasta_inicial):
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    caminho_arquivo = filedialog.askopenfilename(
        initialdir=pasta_inicial,
        title="Selecione o arquivo",
        filetypes=[("Arquivos .prd", "*.prd"), ("Todos os arquivos", "*.*")]
    )
    
    # Insere o caminho do arquivo no widget Text (limpa antes de inserir)
    txt_CaminhoArquivo.delete(1.0, tk.END)  # Limpa o conteúdo existente
    txt_CaminhoArquivo.insert(tk.END, caminho_arquivo)  # Insere o novo caminho
    
    return caminho_arquivo

# Função para centralizar a janela
def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela // 3) - (largura // 90)
    pos_y = (altura_tela // 3) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Função para atualizar as opções do Combobox Process com base no Banco e Bandeira
def atualizar_process(*args):
    banco_selecionado = cbo_banco.get()
    bandeira_selecionada = cbo_bandeira.get()

    # Define as opções de Process com base na seleção do Banco e Bandeira
    
    #AFINZ
    if banco_selecionado == "AFINZ" and bandeira_selecionada == "AMEX":
        process_opcoes = ["AFINZ_AMEX_Process1", "AFINZ_AMEX_Process2"]
    #AFINZ
    #BRADESCO
    elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "ELO":
        process_opcoes = ["BRADESCO_ELO_Process1", "BRADESCO_ELO_Process2"]
    
    elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "MC":
        process_opcoes = ["BRADESCO_MC_Process1", "BRADESCO_MC_Process2"]
     
    elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "VISA":
        process_opcoes = ["BRADESCO_VISA_Process1", "BRADESCO_VISA_Process2"]
     
    elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "AMEX":
        process_opcoes = ["BRADESCO_AMEX_Process1", "BRADESCO_AMEX_Process2"]
    #BRADESCO  
    #ITAU
    elif banco_selecionado == "ITAU" and bandeira_selecionada == "ELO":
        process_opcoes = ["ITAU_ELO_Process1", "ITAU_ELO_Process2"]
    elif banco_selecionado == "ITAU" and bandeira_selecionada == "MC":
        process_opcoes = ["ITAU_MC_Process1", "ITAU_MC_Process2"]
    elif banco_selecionado == "ITAU" and bandeira_selecionada == "VISA":
        process_opcoes = ["ITAU_VISA_Process1", "ITAU_VISA_Process2"]
    elif banco_selecionado == "ITAU" and bandeira_selecionada == "AMEX":
        process_opcoes = ["ITAU_AMEX_Process1", "ITAU_AMEX_Process2"]
    else:
        process_opcoes = ["Sem Process"]
        

    # Atualiza o Combobox de Process com as novas opções
    cbo_process.config(values=process_opcoes)
    cbo_process.set(process_opcoes[0])  # Define o primeiro item como o padrão

pasta_inicial = 'C:/Users/mourabre/Desktop/criarjob/PRD'

# Criar a janela principal
root = Tk()
largura_janela = 400
altura_janela = 300
root.title("Tela Login")
root.geometry("800x600")
root.configure(background="#dedede")
root.maxsize(width=700, height=500)
root.minsize(width=700, height=500)
root.resizable(width=False, height=False)
centralizar_janela(root, largura_janela, altura_janela)

# Frame para organizar o layout
frame = Frame(root)

# Label do caminho do arquivo
labelcaminho = Label(text="Caminho do arquivo PRD:", font=10, bg="#dedede")
labelcaminho.place(x=40, y=35)
# Botão para pesquisar arquivo
btn_pesquisarArquivo = Button(root, text="...", pady=1, padx=10, command=lambda: selecionar_arquivo(pasta_inicial))
btn_pesquisarArquivo.place(x=600, y=60)
# Campo de texto para mostrar o caminho do arquivo
txt_CaminhoArquivo = Text(root, bg="white", height=1, width=60, font=10)
txt_CaminhoArquivo.place(x=40, y=60)

# ProcessID
labelprocessID = Label(text="ProcessID:", bg="#dedede")
labelprocessID.place(x=40, y=90)

labelbanco = Label(text="Banco:", font=10, bg="#dedede")
labelbanco.place(x=40, y=110)
# Combobox para selecionar o banco
banco_opcoes = ["AFINZ", "BRADESCO", "ITAU"]  # Lista de opções
cbo_banco = Combobox(root, values=banco_opcoes, font=10, width=15, state="readonly")
cbo_banco.place(x=40, y=135)
cbo_banco.set("Selecionar Banco")  # Texto padrão do combobox
cbo_banco.bind("<<ComboboxSelected>>", atualizar_process)  # Chama atualizar_process quando o banco for selecionado

labelbandeira = Label(text="Bandeira:", font=10, bg="#dedede")
labelbandeira.place(x=200, y=110)
bandeira_opcoes = ["AMEX", "VISA", "MC", "ELO"]  # Lista de opções
cbo_bandeira = Combobox(root, values=bandeira_opcoes, font=10, width=6, state="readonly")
cbo_bandeira.place(x=200, y=135)
cbo_bandeira.set("AMEX")  # Texto padrão do combobox
cbo_bandeira.bind("<<ComboboxSelected>>", atualizar_process)  # Chama atualizar_process quando a bandeira for selecionada

labelprocess = Label(text="Process:", font=10, bg="#dedede")
labelprocess.place(x=280, y=110)
# Combobox para selecionar o processo
cbo_process = Combobox(root, values=[], font=10, width=37, state="readonly")
cbo_process.place(x=280, y=135)
cbo_process.set("Selecione um process")  # Texto padrão do combobox

# Tipo de Máquina (apenas para exemplo)
label_maquina = Label(text="Maquina:", font=10, bg="#dedede")
label_maquina.place(x=40, y=180)
tipo_maquina_opcoes = ["Máquina A", "Máquina B", "Máquina C"]  # Lista de opções
cbo_tipoMaquina = Combobox(root, values=tipo_maquina_opcoes, font=14, width=20, state="readonly")
cbo_tipoMaquina.place(x=40, y=200)
cbo_tipoMaquina.set("Selecione uma máquina")  # Texto padrão do combobox

root.mainloop()
