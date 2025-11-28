import tkinter as tk
from tkinter import messagebox
from banco import Banco
from transacoes import Transacoes

db = Banco("Banco Python")
ops = Transacoes()

BG_MAIN = "#101010"
BG_CARD = "#181818"
FG_TEXT = "#FFFFFF"
BTN_BG = "#3A7BDC"
BTN_BG_HOVER = "#5B97F0"
BTN_TEXT = "#FFFFFF"
ENTRY_BG = "#2A2A2A"
ENTRY_FG = "#FFFFFF"

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema Bancário")
        self.root.geometry("700x850")
        self.root.configure(bg=BG_MAIN)
        self.tela_inicial()
        self.root.mainloop()

    def botao(self, parent, text, command):
        btn = tk.Label(parent, text=text, bg=BTN_BG, fg=BTN_TEXT,
                       font=("Arial", 15), width=22, pady=12, cursor="hand2")
        btn.bind("<Button-1>", lambda e: command())
        btn.bind("<Enter>", lambda e: btn.config(bg=BTN_BG_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BTN_BG))
        return btn

    def limpar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def entrada(self, parent):
        return tk.Entry(parent, bg=ENTRY_BG, fg=ENTRY_FG, width=34, font=("Arial", 14))

    def tela_inicial(self):
        self.limpar()
        frame = tk.Frame(self.root, bg=BG_CARD, padx=30, pady=30)
        frame.pack(pady=100)

        tk.Label(frame, text="Banco Python", fg=FG_TEXT, bg=BG_CARD,
                 font=("Arial", 34, "bold")).pack(pady=30)

        self.botao(frame, "Criar Cliente", self.tela_criar_cliente).pack(pady=12)
        self.botao(frame, "Criar Conta", self.tela_criar_conta).pack(pady=12)
        self.botao(frame, "Acessar Conta", self.tela_acessar_cpf).pack(pady=12)

    def tela_criar_cliente(self):
        self.limpar()
        frame = tk.Frame(self.root, bg=BG_CARD, padx=30, pady=30)
        frame.pack(pady=70)

        tk.Label(frame, text="Cadastro de Cliente", fg=FG_TEXT, bg=BG_CARD,
                 font=("Arial", 26, "bold")).pack(pady=20)

        tk.Label(frame, text="Nome", fg=FG_TEXT, bg=BG_CARD).pack()
        nome_entry = self.entrada(frame)
        nome_entry.pack(pady=6)

        tk.Label(frame, text="CPF", fg=FG_TEXT, bg=BG_CARD).pack()
        cpf_entry = self.entrada(frame)
        cpf_entry.pack(pady=6)

        def criar():
            nome = nome_entry.get().strip()
            cpf = cpf_entry.get().strip()
            if not nome or not cpf:
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return
            if db.criar_cliente(nome, cpf):
                messagebox.showinfo("OK", "Cliente cadastrado.")
                self.tela_inicial()
            else:
                messagebox.showerror("Erro", "CPF já cadastrado.")

        self.botao(frame, "Cadastrar", criar).pack(pady=15)
        self.botao(frame, "Voltar", self.tela_inicial).pack()

    def tela_criar_conta(self):
        self.limpar()
        frame = tk.Frame(self.root, bg=BG_CARD, padx=30, pady=30)
        frame.pack(pady=60)

        tk.Label(frame, text="Criar Conta Bancária", fg=FG_TEXT, bg=BG_CARD,
                 font=("Arial", 26, "bold")).pack(pady=20)

        tk.Label(frame, text="CPF do Cliente", fg=FG_TEXT, bg=BG_CARD).pack()
        cpf_entry = self.entrada(frame)
        cpf_entry.pack(pady=6)

        tipo_var = tk.StringVar(value="corrente")
        tipos = ["corrente", "poupanca", "salario", "empresarial"]

        opcoes_frame = tk.Frame(frame, bg=BG_CARD)
        opcoes_frame.pack(pady=12)

        for t in tipos:
            tk.Radiobutton(opcoes_frame, text=t.capitalize(), value=t, variable=tipo_var,
                           bg=BG_CARD, fg=FG_TEXT, selectcolor=BG_MAIN,
                           font=("Arial", 13)).pack(anchor="w")

        def criar():
            cpf = cpf_entry.get().strip()
            cliente = db.buscar_cliente(cpf)
            if not cliente:
                messagebox.showerror("Erro", "Cliente não encontrado.")
                return

            tipo = tipo_var.get()
            if tipo == "corrente": conta = db.criar_conta_corrente(cpf)
            elif tipo == "poupanca": conta = db.criar_conta_poupanca(cpf)
            elif tipo == "salario": conta = db.criar_conta_salario(cpf)
            else: conta = db.criar_conta_empresarial(cpf)

            messagebox.showinfo("Conta Criada",
                                f"Conta criada com sucesso.\nNúmero: {conta.numero}")
            self.tela_inicial()

        self.botao(frame, "Criar Conta", criar).pack(pady=12)
        self.botao(frame, "Voltar", self.tela_inicial).pack()

    def tela_acessar_cpf(self):
        self.limpar()
        frame = tk.Frame(self.root, bg=BG_CARD, padx=30, pady=30)
        frame.pack(pady=70)

        tk.Label(frame, text="Acessar Conta", fg=FG_TEXT, bg=BG_CARD,
                 font=("Arial", 26, "bold")).pack(pady=25)

        tk.Label(frame, text="Digite o CPF", fg=FG_TEXT, bg=BG_CARD).pack()
        cpf_entry = self.entrada(frame)
        cpf_entry.pack(pady=8)

        def buscar():
            cpf = cpf_entry.get().strip()
            cliente = db.buscar_cliente(cpf)
            if not cliente:
                messagebox.showerror("Erro", "Cliente não encontrado.")
                return

            contas = db.listar_contas_por_cpf(cpf)
            if not contas:
                messagebox.showinfo("Conta", "Este cliente não possui contas.")
                return

            self.tela_lista_contas(cliente, contas)

        self.botao(frame, "Buscar", buscar).pack(pady=15)
        self.botao(frame, "Voltar", self.tela_inicial).pack()

    def tela_lista_contas(self, cliente, contas):
        self.limpar()
        frame = tk.Frame(self.root, bg=BG_CARD, padx=30, pady=30)
        frame.pack(pady=60)

        tk.Label(frame, text=f"Contas de {cliente.nome}", fg=FG_TEXT, bg=BG_CARD,
                 font=("Arial", 24, "bold")).pack(pady=20)

        lista = tk.Frame(frame, bg=BG_CARD)
        lista.pack(pady=10)

        for conta in contas:
            caixa = tk.Frame(lista, bg="#222222", padx=15, pady=10)
            caixa.pack(fill="x", pady=6)

            tk.Label(caixa, text=f"Conta {conta.numero} | Saldo: R$ {conta.saldo:.2f}",
                     fg=FG_TEXT, bg="#222222", font=("Arial", 14)).pack(side="left")

            btn = tk.Label(caixa, text="Acessar", bg=BTN_BG, fg=BTN_TEXT,
                           font=("Arial", 12), padx=15, pady=5, cursor="hand2")
            btn.pack(side="right")
            btn.bind("<Button-1>", lambda e, c=conta: self.tela_conta(c))

        self.botao(frame, "Voltar", self.tela_acessar_cpf).pack(pady=25)

    def tela_conta(self, conta):
        self.limpar()
        frame = tk.Frame(self.root, bg=BG_CARD, padx=30, pady=30)
        frame.pack(pady=50)

        tk.Label(frame, text=f"Conta {conta.numero}", fg=FG_TEXT,
                 bg=BG_CARD, font=("Arial", 28, "bold")).pack(pady=10)

        tk.Label(frame, text=f"Cliente: {conta.cliente.nome}",
                 fg=FG_TEXT, bg=BG_CARD, font=("Arial", 16)).pack(pady=5)

        saldo_lbl = tk.Label(frame, text=f"Saldo: R$ {conta.saldo:.2f}",
                             fg="#67E08A", bg=BG_CARD, font=("Arial", 20))
        saldo_lbl.pack(pady=25)

        def depositar():
            valor = self.popup_valor("Depósito")
            if valor and ops.depositar(conta, valor):
                saldo_lbl.config(text=f"Saldo: R$ {conta.saldo:.2f}")

        def sacar():
            valor = self.popup_valor("Saque")
            if valor and ops.sacar(conta, valor):
                saldo_lbl.config(text=f"Saldo: R$ {conta.saldo:.2f}")

        def extrato():
            registros = ops.listar_extrato(conta)
            if not registros:
                messagebox.showinfo("Extrato", "Sem movimentações.")
                return

            texto = ""
            for r in registros:
                texto += f"{r['data']} | {r['tipo']} | R$ {r['valor']}\n"

            messagebox.showinfo("Extrato da Conta", texto)

        self.botao(frame, "Depositar", depositar).pack(pady=8)
        self.botao(frame, "Sacar", sacar).pack(pady=8)
        self.botao(frame, "Extrato", extrato).pack(pady=8)
        self.botao(frame, "Voltar", self.tela_acessar_cpf).pack(pady=25)

    def popup_valor(self, titulo):
        popup = tk.Toplevel(self.root)
        popup.title(titulo)
        popup.configure(bg=BG_CARD)

        tk.Label(popup, text=f"{titulo} - Valor", fg=FG_TEXT, bg=BG_CARD,
                 font=("Arial", 14)).pack(pady=10)

        entrada = tk.Entry(popup, bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 14))
        entrada.pack(pady=10)

        resultado = []

        def ok():
            try:
                valor = float(entrada.get())
                resultado.append(valor)
                popup.destroy()
            except:
                messagebox.showerror("Erro", "Valor inválido.")

        self.botao(popup, "OK", ok).pack(pady=10)

        popup.grab_set()
        popup.wait_window()
        return resultado[0] if resultado else None


if __name__ == "__main__":
    App()
