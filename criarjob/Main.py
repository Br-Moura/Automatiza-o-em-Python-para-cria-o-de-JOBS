from tkinter import *

# Função para abrir uma nova janela e fechar a janela principal
def Tela_Principal():
    # Cria a nova janela (Toplevel)
    Tela_login = Toplevel()
    Tela_login.geometry("260x360")
    Tela_login.configure(background="#dde")
    Tela_login.title("JobAUTO")
    Tela_login.maxsize(width=900, height=550)
    Tela_login.minsize(width=360, height=480)
    centralizar_janela(Tela_inicial, largura_janela, altura_janela)
    
    # Adicionando um label na nova janela
    label = Label(Tela_login, text="Esta é uma nova janela!")
    label.pack(pady=20)
    
    # Cria o botão que chama a função de voltar para a tela principal
    btn_tela = Button(Tela_login, text="Voltar para a tela principal", command=lambda: voltar_tela_Login(Tela_login))
    btn_tela.place(x=100, y=100)

    # Esconde a janela principal (Tela_inicial) quando a nova janela for aberta
    Tela_inicial.withdraw()

# Função para voltar para a tela principal
def voltar_tela_Login(Tela_login):
    Tela_login.destroy()  # Fecha a nova janela
    Tela_inicial.deiconify()  # Revela a janela principal

def centralizar_janela(Tela_inicial, largura, altura):
    # Obtém a largura e a altura da tela
    largura_tela = Tela_inicial.winfo_screenwidth()
    altura_tela = Tela_inicial.winfo_screenheight()
    
    # Calcula a posição x e y para centralizar a janela
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 3) - (altura // 2)
    
    # Define a geometria da janela para centralizá-la
    Tela_inicial.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Configurando a janela principal
Tela_inicial = Tk()
largura_janela = 400
altura_janela = 300
Tela_inicial.title("Tela Login")
Tela_inicial.geometry("240x360")
Tela_inicial.configure(background="#dde")
Tela_inicial.maxsize(width=900, height=550)
Tela_inicial.minsize(width=360, height=480)
Tela_inicial.resizable(width=False, height=False)
centralizar_janela(Tela_inicial, largura_janela, altura_janela)

# Botão para abrir a nova janela e esconder a janela principal
btn_novaTela = Button(Tela_inicial, text="Usar essa conta", command=Tela_Principal, pady=19)
btn_novaTela.place(x=160, y=350)

# Executa a interface gráfica
Tela_inicial.mainloop()
