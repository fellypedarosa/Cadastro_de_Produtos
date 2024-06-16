import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

def limpar_campos():
    entry_cliente.delete(0, tk.END)
    entry_produto.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    categoria_combobox.set("Escolha a categoria")

def salvar_arquivo():
    cliente = entry_cliente.get().strip().title()
    produto = entry_produto.get().strip().title()
    quantidade = entry_quantidade.get().strip()
    categoria = categoria_combobox.get().strip().title()

    categorias_validas = ['Esportes', 'Comida', 'Bebida', 'Jardinagem', 'Moveis', 'Roupas', 'Eletronicos']
    
    if not cliente or not produto or not quantidade or not categoria:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        return
    
    if categoria not in categorias_validas:
        messagebox.showerror("Erro", "Categoria inválida. Escolha entre: Esportes, Comida, Bebida, Jardinagem, Moveis, Roupas, Eletronicos. \nNão esqueça de remover os acentos")
        return

    try:
        quantidade = int(quantidade)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")
        return

    # Criar um nome de arquivo único baseado na data e hora atuais
    timestamp = datetime.now().strftime("%H-%M-%S-%d-%m-%Y")
    filename = f"Tabela_{timestamp}.txt"

    with open(filename, 'w') as file:
        file.write(f"Cliente: {cliente}\n")
        file.write(f"Produto: {produto}\n")
        file.write(f"Quantidade: {quantidade}\n")
        file.write(f"Categoria: {categoria}\n")

    messagebox.showinfo("Sucesso", f"Informações salvas com sucesso em {filename}!")
    limpar_campos()

def on_entry_click(event):
    if categoria_combobox.get() == 'Escolha a categoria':
        categoria_combobox.set('')
        categoria_combobox.config(foreground='black')

def on_focusout(event):
    if not categoria_combobox.get():
        categoria_combobox.set('Escolha a categoria')
        categoria_combobox.config(foreground='grey')

app = tk.Tk()
app.title("Cadastro de Produtos")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Campo Cliente
label_cliente = tk.Label(frame, text="Cliente:")
label_cliente.grid(row=0, column=0, sticky='e')
entry_cliente = tk.Entry(frame)
entry_cliente.grid(row=0, column=1, pady=5)

# Campo Produto
label_produto = tk.Label(frame, text="Produto:")
label_produto.grid(row=1, column=0, sticky='e')
entry_produto = tk.Entry(frame)
entry_produto.grid(row=1, column=1, pady=5)

# Campo Quantidade
label_quantidade = tk.Label(frame, text="Quantidade:")
label_quantidade.grid(row=2, column=0, sticky='e')
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=2, column=1, pady=5)

# Campo Categoria
label_categoria = tk.Label(frame, text="Categoria:")
label_categoria.grid(row=3, column=0, sticky='e')
categoria_combobox = ttk.Combobox(frame, values=['Esportes', 'Comida', 'Bebida', 'Jardinagem', 'Móveis', 'Roupas', 'Eletrônicos'])
categoria_combobox.grid(row=3, column=1, pady=5)
categoria_combobox.set("Escolha a categoria")
categoria_combobox.config(foreground='grey')
categoria_combobox.bind('<FocusIn>', on_entry_click)
categoria_combobox.bind('<FocusOut>', on_focusout)

# Botão Salvar
button_salvar = tk.Button(frame, text="Salvar", command=salvar_arquivo)
button_salvar.grid(row=4, columnspan=2, pady=10)

app.mainloop()
