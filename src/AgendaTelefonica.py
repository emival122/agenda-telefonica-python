from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dados import adicionar_dados, ver_dados, remover_dados, atualizar_dados

# ================== CORES ==================
co0 = "#f0f3f5"
co1 = "#ffffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#ec8b33"
co6 = "#ef5350"
co7 = "#93cd95"

# ================== JANELA ==================
janela = Tk()
# Adicionando o ícone
img_icone = PhotoImage(file='assets/icon.png')
janela.iconphoto(False, img_icone)

janela.title("Agenda Telefônica")
janela.geometry("1100x700")
janela.configure(bg=co0)
janela.resizable(True, True)

telefone_para_atualizar = ""

# ================== FUNÇÕES ==================


def mostrar_tabela(dados_para_exibir=None):
    global tree
    for widget in frame_tabela.winfo_children():
        widget.destroy()

    lista = ver_dados() if dados_para_exibir is None else dados_para_exibir
    tabela_head = ['Nome', 'Sexo', 'Telefone', 'Email']

    scrollbar_y = Scrollbar(frame_tabela, orient=VERTICAL)
    scrollbar_y.pack(side=RIGHT, fill=Y)

    scrollbar_x = Scrollbar(frame_tabela, orient=HORIZONTAL)
    scrollbar_x.pack(side=BOTTOM, fill=X)

    tree = ttk.Treeview(
        frame_tabela,
        columns=tabela_head,
        show="headings",
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )
    tree.pack(fill=BOTH, expand=True)

    scrollbar_y.config(command=tree.yview)
    scrollbar_x.config(command=tree.xview)

    larguras = [250, 120, 200, 400]
    for i, col in enumerate(tabela_head):
        tree.heading(col, text=col)
        tree.column(col, width=larguras[i])

    for item in lista:
        tree.insert('', 'end', values=item)


def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_telefone.get()
    email = e_email.get()

    if not nome or not sexo or not telefone or not email:
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    adicionar_dados([nome, sexo, telefone, email])
    messagebox.showinfo("Sucesso", "Contato adicionado!")
    limpar_campos()
    mostrar_tabela()


def deletar():
    try:
        item = tree.item(tree.focus())['values']
        remover_dados(str(item[2]))
        messagebox.showinfo("Sucesso", "Contato removido!")
        mostrar_tabela()
    except:
        messagebox.showwarning("Erro", "Selecione um contato!")


def preparar_atualizacao():
    global telefone_para_atualizar
    try:
        item = tree.item(tree.focus())['values']
        limpar_campos()
        e_nome.insert(0, item[0])
        c_sexo.set(item[1])
        e_telefone.insert(0, item[2])
        e_email.insert(0, item[3])
        telefone_para_atualizar = str(item[2])
        b_confirmar.pack(pady=5)
    except:
        messagebox.showwarning("Erro", "Selecione um contato!")


def confirmar_edicao():
    novos_dados = [
        telefone_para_atualizar,
        e_nome.get(),
        c_sexo.get(),
        e_telefone.get(),
        e_email.get()
    ]
    atualizar_dados(novos_dados)
    messagebox.showinfo("Sucesso", "Dados atualizados!")
    b_confirmar.pack_forget()
    limpar_campos()
    mostrar_tabela()


def procurar_contato():
    telefone = e_procurar.get()
    if not telefone:
        messagebox.showwarning("Erro", "Digite o telefone!")
        return

    filtrado = [i for i in ver_dados() if str(i[2]) == telefone]
    if filtrado:
        mostrar_tabela(filtrado)
    else:
        messagebox.showinfo("Busca", "Contato não encontrado")


def limpar_campos():
    e_nome.delete(0, END)
    e_telefone.delete(0, END)
    e_email.delete(0, END)
    c_sexo.set("")


# ================== FRAMES ==================
frame_cima = Frame(janela, bg=co3)
frame_cima.pack(fill=X)

frame_baixo = Frame(janela, bg=co0)
frame_baixo.pack(fill=X, padx=20)

frame_baixo.grid_columnconfigure(0, weight=3)
frame_baixo.grid_columnconfigure(1, weight=1)
frame_baixo.grid_columnconfigure(2, weight=1)

frame_tabela = Frame(janela, bg=co1)
frame_tabela.pack(fill=BOTH, expand=True, padx=20, pady=10)

# ================== TÍTULO ==================
Label(
    frame_cima,
    text="Agenda Telefônica",
    font=("Arial", 28, "bold"),
    bg=co3,
    fg=co1
).pack(pady=20)

# ================== CARD FORM ==================
card_form = Frame(frame_baixo, bg=co1, padx=30, pady=25)
card_form.grid(row=0, column=0, sticky="nsew", padx=10)

card_form.grid_columnconfigure(1, weight=1)

fonte_label = ("Arial", 11, "bold")
fonte_entry = ("Arial", 11)

Label(card_form, text="Nome", bg=co1, font=fonte_label).grid(
    row=0, column=0, sticky="w", pady=10)
e_nome = Entry(card_form, font=fonte_entry)
e_nome.grid(row=0, column=1, sticky="ew", pady=10, padx=10)

Label(card_form, text="Sexo", bg=co1, font=fonte_label).grid(
    row=1, column=0, sticky="w", pady=10)
c_sexo = ttk.Combobox(card_form, values=["M", "F"], font=fonte_entry)
c_sexo.grid(row=1, column=1, sticky="ew", pady=10, padx=10)

Label(card_form, text="Telefone", bg=co1, font=fonte_label).grid(
    row=2, column=0, sticky="w", pady=10)
e_telefone = Entry(card_form, font=fonte_entry)
e_telefone.grid(row=2, column=1, sticky="ew", pady=10, padx=10)

Label(card_form, text="Email", bg=co1, font=fonte_label).grid(
    row=3, column=0, sticky="w", pady=10)
e_email = Entry(card_form, font=fonte_entry)
e_email.grid(row=3, column=1, sticky="ew", pady=10, padx=10)

# ================== BOTÕES ==================
card_botoes = Frame(frame_baixo, bg=co0)
card_botoes.grid(row=0, column=1, padx=10, sticky="n")

Button(card_botoes, text="Adicionar", command=inserir, bg=co2, fg=co1,
       font=("Arial", 11, "bold"), width=15, height=2).pack(pady=6)

Button(card_botoes, text="Atualizar", command=preparar_atualizacao, bg=co7, fg=co4,
       font=("Arial", 11, "bold"), width=15, height=2).pack(pady=6)

Button(card_botoes, text="Deletar", command=deletar, bg=co6, fg=co1,
       font=("Arial", 11, "bold"), width=15, height=2).pack(pady=6)

b_confirmar = Button(card_botoes, text="Confirmar", command=confirmar_edicao,
                     bg=co2, fg=co1, font=("Arial", 11, "bold"), width=15, height=2)

# ================== BUSCA ==================
card_busca = Frame(frame_baixo, bg=co1, padx=20, pady=25)
card_busca.grid(row=0, column=2, padx=10, sticky="n")

Label(card_busca, text="Buscar por telefone", bg=co1,
      font=("Arial", 11, "bold")).pack(anchor="w", pady=5)

e_procurar = Entry(card_busca, font=fonte_entry)
e_procurar.pack(fill=X, pady=8)

Button(card_busca, text="Procurar", command=procurar_contato,
       font=("Arial", 11, "bold"), width=15).pack(pady=5)

Button(card_busca, text="Ver Todos", command=mostrar_tabela,
       font=("Arial", 11, "bold"), width=15).pack(pady=5)

# ================== ESTILO TABELA ==================
style = ttk.Style()
style.configure("Treeview", font=("Arial", 11), rowheight=32)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

mostrar_tabela()
janela.mainloop()
