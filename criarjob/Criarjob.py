import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
import re
from tkinter.ttk import Combobox
from tkinter import messagebox
import shutil

def selecionar_arquivo(pasta_inicial):
    global caminho_arquivo
    root = tk.Tk()
    root.withdraw()
    caminho_arquivo = filedialog.askopenfilename(
        initialdir=pasta_inicial,
        title="Selecione o arquivo",
        filetypes=[("Arquivos .prd", "*.prd"), ("Todos os arquivos", "*.*")]
    )

    if caminho_arquivo:
        txt_CaminhoArquivo.delete(1.0, tk.END) 
        txt_CaminhoArquivo.insert(tk.END, caminho_arquivo)
        return caminho_arquivo
    else:
        return None

def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela // 3) - (largura // 90)
    pos_y = (altura_tela // 3) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

def atualizar_process(*args):
    ambiente_selecionado = variable.get() 
    banco_selecionado = cbo_banco.get()
    bandeira_selecionada = cbo_bandeira.get()


    if ambiente_selecionado == "Homologação":
        if banco_selecionado == "AFINZ" and bandeira_selecionada == "AMEX":
            process_opcoes = ["AFINZ_AMEX_Homolog1", "AFINZ_AMEX_Homolog2"]
        elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "ELO":
            process_opcoes = ["BRADESCO_ELO_Homolog1", "BRADESCO_ELO_Homolog2"]
        elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "MC":
            process_opcoes = ["BRADESCO_MC_Homolog", "BRADESCO_MC_Homolog2"]
        elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "VISA":
            process_opcoes = ["BRADESCO_VISA_Homolog1", "BRADESCO_VISA_Homolog2"]
        elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "AMEX":
            process_opcoes = ["BRADESCO_AMEX_Homolog1", "BRADESCO_AMEX_Homolog2"]
        elif banco_selecionado == "ITAU" and bandeira_selecionada == "MC":
            process_opcoes = ["ITAU_MC_Homolog1", "ITAU_MC_Homolog2"]
        elif banco_selecionado == "ITAU" and bandeira_selecionada == "VISA":
            process_opcoes = ["ITAU_VISA_Homolog1", "ITAU_VISA_Homolog2"]
        else:
            process_opcoes = ["Sem Process"]

    elif ambiente_selecionado == "Produção":
        if banco_selecionado == "AFINZ" and bandeira_selecionada == "AMEX":
            process_opcoes = ["AFINZ_AMEX_Produção1", "AFINZ_AMEX_Produção2"]
        elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "ELO":
            process_opcoes = ["BRADESCO_ELO_Produção1", "BRADESCO_ELO_Produção2"]
        elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "MC":
            process_opcoes = ["BRADESCO_MC_Produção1", "BRADESCO_MC_Produção2"]
        elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "VISA":
            process_opcoes = ["BRADESCO_VISA_Produção1", "BRADESCO_VISA_Produção2"]
        elif banco_selecionado == "BRADESCO" and bandeira_selecionada == "AMEX":
            process_opcoes = ["BRADESCO_AMEX_Produção1", "BRADESCO_AMEX_Produção2"]
        elif banco_selecionado == "ITAU" and bandeira_selecionada == "MC":
            process_opcoes = ["ITAU_MC_Produção1", "ITAU_MC_Produção2"]
        elif banco_selecionado == "ITAU" and bandeira_selecionada == "VISA":
            process_opcoes = ["ITAU_VISA_Produção1", "ITAU_VISA_Produção2"]
        else:
            process_opcoes = ["Sem Process"]

    cbo_process.config(values=process_opcoes)
    cbo_process.set(process_opcoes[0]) 

    if process_opcoes[0] == "Sem Process":
        cbo_process.config(state="disabled")
    else:
        cbo_process.config(state="readonly")

def mudar_ambiente():
    ambiente_selecionado = variable.get()
    if ambiente_selecionado == "Homologação":
        return "C:/Users/mourabre/Desktop/criarjob/INI"
    elif ambiente_selecionado == "Produção":
        return "C:/Users/mourabre/Desktop/criarjob"

def extrair_nome_arquivo(caminho_arquivo):
    nome_arquivo = os.path.basename(caminho_arquivo)  
    nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]  
    return nome_arquivo_sem_extensao

def extrair_caminho_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as file:
        conteudo = file.read()
    match = re.search(r'(PAYMENT\\(?:[A-Z0-9_]+\\)*\d{2}-\d{2}\\[A-Z0-9_]+\.PRD)', conteudo)

    if match:
        return match.group(1)
    else:
        return "Caminho não encontrado."

def gerar_registros_simulados(caminho_arquivo):
    registros = []
    for i in range(1, 11):  
        registro = f"{i:08d}{i:08d}" 
        registros.append(registro)

    quantidade_registros = len(registros)  
    return quantidade_registros

def create_ini_file():
    global caminho_arquivo  
    section = extrair_nome_arquivo(caminho_arquivo)
    customer = "PyautoUPP"
    machineid = ""
    machinetype = cbo_tipoMaquina.get()
    parentjobid = ""
    pieces = gerar_registros_simulados(caminho_arquivo)
    processid = cbo_process.get()
    prodfile = extrair_caminho_arquivo(caminho_arquivo)
    prodtype = "4"
    pulist = "1-E"
    status = ""
    directory = mudar_ambiente() 

    filename = os.path.join(directory, f'{section}.ini')

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

    # Verifica se o arquivo já existe e solicita confirmação para sobrescrever
    if os.path.exists(filename):
        resposta = messagebox.askquestion("Sobrescrever arquivo", f"O arquivo {section} já existe. Deseja sobrescrever?", icon='warning')
        if resposta == 'no':
            return

    # Cria o arquivo .ini
    with open(filename, 'w') as file:
        file.write(ini_content)

    # Exibe mensagem de sucesso
    messagebox.showinfo("Arquivo gerado", f"Arquivo .ini gerado com sucesso: {section}")

def verificar_campos():

    if not caminho_arquivo or caminho_arquivo == "": 
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PRD.")
        return False

    if cbo_banco.get() == "Selecionar Banco": 
        messagebox.showerror("Erro", "Por favor, selecione um banco.")
        return False

    if cbo_bandeira.get() == "":  
        messagebox.showerror("Erro", "Por favor, selecione uma bandeira.")
        return False

    if cbo_process.get() == "Sem Process" or cbo_process.get() == "":  
        messagebox.showerror("Erro", "Por favor, selecione um processo válido.")
        return False

    if cbo_tipoMaquina.get() == "Selecione uma máquina":  
        messagebox.showerror("Erro", "Por favor, selecione o tipo de máquina.")
        return False

    return True

def limpar_campos():
    global caminho_arquivo
    txt_CaminhoArquivo.delete(1.0, tk.END)
    cbo_banco.set("Selecionar Banco") 
    cbo_bandeira.set("")  
    cbo_process.set("Sem Process")  
    cbo_tipoMaquina.set("Selecione uma máquina") 

def copiar_arquivo_destino():
    global caminho_arquivo
    
    caminho_extraido = extrair_caminho_arquivo(caminho_arquivo)
    caminho_base_destino = r'C:/Users/mourabre/Desktop/teste'
    pasta_destino, nome_arquivo = os.path.split(caminho_extraido)
    caminho_pasta_destino_completo = os.path.join(caminho_base_destino, pasta_destino)
    try:
        if not os.path.exists(caminho_pasta_destino_completo):
            os.makedirs(caminho_pasta_destino_completo)
            print(f"Pasta {caminho_pasta_destino_completo} criada.")
            
        caminho_arquivo_destino = os.path.join(caminho_pasta_destino_completo, nome_arquivo)
        shutil.copy(caminho_arquivo, caminho_arquivo_destino)
        print(f"Arquivo copiado para {caminho_arquivo_destino}")
        
    except FileNotFoundError:
        print("Arquivo de origem não encontrado!")
    except PermissionError:
        print("Permissão negada para acessar os arquivos!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def criar_job():
    if verificar_campos():
        create_ini_file()
        copiar_arquivo_destino()
        
        limpar_campos()

def main():
    global txt_CaminhoArquivo, cbo_banco, cbo_bandeira, cbo_process, cbo_tipoMaquina, variable

    root = tk.Tk()
    root.title("Gerador de Arquivos .ini")
    centralizar_janela(root, 400, 300)
    root.configure(background="#dedede")
    root.maxsize(width=700, height=500)
    root.minsize(width=700, height=500)

    lbl_titulo = Label(root, text="Gerador de Arquivos .ini",background="#dedede", font=("Arial", 16, "bold"))
    lbl_titulo.pack(pady=10)

    frame = Frame(root)
    frame.pack(pady=10)

    Label(root, text="Ambiente:", background="#dedede").place(x=505, y=10)
    Label(root, text="Banco:", font=10, bg="#dedede").place(x=40, y=150)
    Label(root, text="Bandeira:", font=10, bg="#dedede").place(x=200, y=150)
    Label(root, text="Process:", font=10, bg="#dedede").place(x=280, y=150)
    Label(root, text="Caminho do arquivo PRD:", font=10, bg="#dedede").place(x=40, y=75)
    Label(root, text="Maquina:", font=10, bg="#dedede").place(x=40, y=225)

    ambientes = ["Homologação", "Produção"]
    variable = StringVar(root)
    variable.set(ambientes[0])
    opt_Ambiente = OptionMenu(root, variable, *ambientes, command=atualizar_process)
    opt_Ambiente.place(x=570, y=6)

    bancos = ["AFINZ", "BRADESCO", "ITAU"]
    cbo_banco = Combobox(root, values=bancos, font=10, width=15, state="readonly")
    cbo_banco.place(x=40, y=175)
    cbo_banco.set("Selecionar Banco")  
    cbo_banco.bind("<<ComboboxSelected>>", atualizar_process) 

    bandeiras = ["AMEX", "ELO", "MC", "VISA"]
    cbo_bandeira = Combobox(root, values=bandeiras, font=10, width=6, state="readonly")
    cbo_bandeira.place(x=200, y=175)
    cbo_bandeira.set(bandeiras[0])
    cbo_bandeira.bind("<<ComboboxSelected>>", atualizar_process)

    cbo_process = Combobox(root, values=[], font=10, width=37, state="readonly")
    cbo_process.place(x=280, y=175)
    cbo_process.set("Sem Process") 

    tipo_maquinas = ["Tipo1", "Tipo2", "Tipo3"]
    cbo_tipoMaquina = Combobox(root, values=tipo_maquinas, font=14, width=20, state="readonly")
    cbo_tipoMaquina.place(x=40, y=250)
    cbo_tipoMaquina.set("Selecione uma máquina")  

    txt_CaminhoArquivo = Text(root, bg="white", height=1, width=60, font=10)
    txt_CaminhoArquivo.place(x=40, y=100)

    btn_SelecionarArquivo = Button(root, text="...", pady=1, padx=10, command=lambda: selecionar_arquivo(pasta_inicial))
    btn_SelecionarArquivo.place(x=600, y=100)

    btn_CriarINI = Button(root, text="Criar JOB", width=20, height=3,command=criar_job)
    btn_CriarINI.place(x=40, y=400)

    btn_sair = Button(root, text="Sair", width=20, height=3,command=root.quit)
    btn_sair.place(x=490, y=400)

    root.mainloop()

if __name__ == "__main__":
    caminho_arquivo = None
    pasta_inicial = 'C:/Users/mourabre/Desktop/criarjob/PRD'
    main()