from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Criar janela principal
app = Tk()
app.geometry("1100x600")
app.title("Sistema de Cadastro de Usuários")

# Estilo da interface
app.configure(bg="#D3E0EA")  # Cor de fundo suave

# Configurações de estilo de widgets
estilo = ttk.Style()
estilo.configure("TLabel", background="#D3E0EA", font="Arial 12", foreground="#0A4D68")
estilo.configure("TButton", background="#0A4D68", font="Arial 14", foreground="white")
estilo.configure("Treeview.Heading", font="Arial 12 bold", foreground="#0A4D68")

# Função para criar campos com rótulos (labels) e caixas de entrada (entry)
def criar_campo(label, linha, coluna, largura=20):
    lbl = ttk.Label(app, text=label)
    lbl.grid(row=linha, column=coluna, padx=10, pady=10, sticky="E")
    entry = Entry(app, font="Arial 12", width=largura)
    entry.grid(row=linha, column=coluna + 1, padx=10, pady=10, sticky="W")
    return entry

# Criar campos de entrada
entryCodigo = criar_campo("Código:", 0, 0)
entryNomeCompleto = criar_campo("Nome Completo:", 0, 2, largura=30)
entryIdade = criar_campo("Idade:", 1, 0)

# Adiciona um label para o campo de gênero
lblGenero = ttk.Label(app, text="Gênero:")
lblGenero.grid(row=1, column=2, padx=10, pady=10, sticky="E")
comboGenero = ttk.Combobox(app, values=["Masculino", "Feminino", "Outro"], font="Arial 12", state="readonly", width=18)
comboGenero.grid(row=1, column=3, padx=10, pady=10, sticky="W")

entryEmail = criar_campo("E-mail:", 2, 0)
entryTelefone = criar_campo("Telefone:", 2, 2)
entryEndereco = criar_campo("Endereço:", 3, 0, largura=50)

# Aumenta a largura dos campos de Nome do Pai e Nome da Mãe
entryNomePai = criar_campo("Nome do Pai:", 4, 0, largura=30)
entryNomeMae = criar_campo("Nome da Mãe:", 4, 2, largura=30)
entryRG = criar_campo("RG:", 5, 0)
entryCPF = criar_campo("CPF:", 5, 2)
entryFormacao = criar_campo("Formação:", 6, 0, largura=50)

# Função para adicionar registros ao Treeview
def adicionarRegistro():
    if not entryCodigo.get() or not entryNomeCompleto.get():
        messagebox.showwarning("Aviso", "Preencha os campos obrigatórios!")
    else:
        # Adiciona os dados ao Treeview
        tree.insert("", "end",
                    values=(entryCodigo.get(), entryNomeCompleto.get(), entryIdade.get(), comboGenero.get(),
                            entryEmail.get(), entryTelefone.get(), entryEndereco.get(),
                            entryNomePai.get(), entryNomeMae.get(), entryRG.get(), entryCPF.get(), entryFormacao.get()))
        
        # Limpa os campos após o registro
        for campo in [entryCodigo, entryNomeCompleto, entryIdade, entryEmail, entryTelefone, entryEndereco,
                      entryNomePai, entryNomeMae, entryRG, entryCPF, entryFormacao]:
            campo.delete(0, END)
        comboGenero.set("")

# Botão para cadastrar
botaoCadastrar = Button(app, text="Cadastrar", font="Arial 14", bg="#0A4D68", fg="white", command=adicionarRegistro)
botaoCadastrar.grid(row=7, column=0, columnspan=4, padx=10, pady=20, sticky="NSEW")

# Configuração do Treeview com colunas adicionais
colunas = ("Código", "Nome Completo", "Idade", "Gênero", "E-mail", "Telefone", "Endereço", 
           "Nome do Pai", "Nome da Mãe", "RG", "CPF", "Formação")
tree = ttk.Treeview(app, columns=colunas, show="headings", height=10)

# Configura as colunas no Treeview
for coluna in colunas:
    tree.heading(coluna, text=coluna)
    tree.column(coluna, anchor=CENTER, width=100)

# Insere alguns dados de exemplo
tree.insert("", "end", values=("001", "Marcos Silva", 32, "Masculino", "marcos@gmail.com", "9999-9999", "Rua A, 123",
                               "Carlos Silva", "Maria Silva", "12345678", "98765432100", "Engenharia"))

tree.insert("", "end", values=("002", "Júlia Costa", 28, "Feminino", "julia@hotmail.com", "8888-8888", "Av. B, 456",
                               "Roberto Costa", "Clara Costa", "87654321", "12345678900", "Administração"))

# Posiciona o Treeview
tree.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky="NSEW")

# Ajuste de largura das colunas específicas para dados maiores
tree.column("Endereço", width=200)
tree.column("Formação", width=150)

# Loop principal da aplicação
app.mainloop()
