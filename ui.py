import tkinter as tk
from tkinter import messagebox
from banco import Banco
from transacoes import Transacoes

db = Banco("Banco Python")
ops = Transacoes()

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema Bancário")
        self.root.geometry("400x350")

        self.tela_inicial()
        self.root.mainloop()

    def tela_inicial(self):
        for widget in self.root.winfo_children(): widget.destroy()

        tk.Label(self.root, text="Sistema Bancário", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root, text="Criar Cliente", width=20, command=self.tela_criar_cliente).pack(pady=5)
        tk.Button(self.root, text="Criar Conta", width=20, command=self.tela_criar_conta).pack(pady=5)
        tk.Button(self.root, text="Acessar Conta", width=20, command=self.tela_acessar_conta).pack(pady=5)


    def tela_criar_cliente(self):
        for widget in self.root.winfo_children(): widget.destroy()

        tk.Label(self.root, text="Criar Cliente", font=("Arial", 16)).pack(pady=10)

        nome_entry = tk.Entry(self.root)
        cpf_entry = tk.Entry(self.root)

        tk.Label(self.root, text="Nome:").pack(); nome_entry.pack()
        tk.Label(self.root, text="CPF:").pack(); cpf_entry.pack()

        def criar():
            nome = nome_entry.get()
            cpf = cpf_entry.get()
            if not nome or not cpf:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
                return
            if db.criar_cliente(nome, cpf):
                messagebox.showinfo("OK", "Cliente criado com sucesso!")
                self.tela_inicial()
            else:
                messagebox.showerror("Erro", "CPF já cadastrado.")

        tk.Button(self.root, text="Criar", command=criar).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial).pack()

    def tela_criar_conta(self):
        for widget in self.root.winfo_children(): widget.destroy()

        tk.Label(self.root, text="Criar Conta", font=("Arial", 16)).pack(pady=10)

        cpf_entry = tk.Entry(self.root)
        tk.Label(self.root, text="CPF do cliente:").pack(); cpf_entry.pack()

        tipo_var = tk.StringVar(value="corrente")
        tk.Radiobutton(self.root, text="Corrente", variable=tipo_var, value="corrente").pack()
        tk.Radiobutton(self.root, text="Poupança", variable=tipo_var, value="poupanca").pack()
        tk.Radiobutton(self.root, text="Salário", variable=tipo_var, value="salario").pack()
        tk.Radiobutton(self.root, text="Empresarial", variable=tipo_var, value="empresarial").pack()

        def criar():
            cpf = cpf_entry.get()
            tipo = tipo_var.get()
            if not db.buscar_cliente(cpf):
                messagebox.showerror("Erro", "Cliente não encontrado.")
                return
            if tipo == "corrente": conta = db.criar_conta_corrente(cpf)
            elif tipo == "poupanca": conta = db.criar_conta_poupanca(cpf)
            elif tipo == "salario": conta = db.criar_conta_salario(cpf)
            else: conta = db.criar_conta_empresarial(cpf)
            messagebox.showinfo("OK", f"Conta criada! Número: {conta.numero}")
            self.tela_inicial()

        tk.Button(self.root, text="Criar", command=criar).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial).pack()


    def tela_acessar_conta(self):
        for widget in self.root.winfo_children(): widget.destroy()

        tk.Label(self.root, text="Acessar Conta", font=("Arial", 16)).pack(pady=10)
        numero_entry = tk.Entry(self.root)

        tk.Label(self.root, text="Número da conta:").pack(); numero_entry.pack()

        def acessar():
            try:
                numero = int(numero_entry.get())
            except:
                messagebox.showerror("Erro", "Número inválido")
                return
            conta = db.buscar_conta(numero)
            if not conta:
                messagebox.showerror("Erro", "Conta não encontrada.")
                return
            self.tela_conta(conta)

        tk.Button(self.root, text="Acessar", command=acessar).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial).pack()

    def tela_conta(self, conta):
        for widget in self.root.winfo_children(): widget.destroy()

        tk.Label(self.root, text=f"Conta {conta.numero}", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=f"Cliente: {conta.cliente.nome}").pack()
        saldo_lbl = tk.Label(self.root, text=f"Saldo: R$ {conta.saldo}")
        saldo_lbl.pack(pady=5)

        def depositar():
            valor = self.popup_valor("Depositar")
            if valor and ops.depositar(conta, valor):
                saldo_lbl.config(text=f"Saldo: R$ {conta.saldo}")

        def sacar():
            valor = self.popup_valor("Sacar")
            if valor and ops.sacar(conta, valor):
                saldo_lbl.config(text=f"Saldo: R$ {conta.saldo}")

        def extrato():
            registros = ops.listar_extrato()
            txt = "\n".join([f"{r['data']} - {r['tipo']} - R$ {r['valor']}" for r in registros]) or "Sem operações."
            messagebox.showinfo("Extrato", txt)

        tk.Button(self.root, text="Depositar", width=20, command=depositar).pack(pady=5)
        tk.Button(self.root, text="Sacar", width=20, command=sacar).pack(pady=5)
        tk.Button(self.root, text="Extrato", width=20, command=extrato).pack(pady=5)
        tk.Button(self.root, text="Voltar", width=20, command=self.tela_inicial).pack(pady=10)


    def popup_valor(self, titulo):
        popup = tk.Toplevel(self.root)
        popup.title(titulo)
        tk.Label(popup, text="Valor:").pack()
        entrada = tk.Entry(popup)
        entrada.pack()
        resultado = []

        def ok():
            try:
                valor = float(entrada.get())
                resultado.append(valor)
                popup.destroy()
            except:
                messagebox.showerror("Erro", "Valor inválido")

        tk.Button(popup, text="OK", command=ok).pack(pady=5)
        popup.wait_window()
        return resultado[0] if resultado else None


if __name__ == "__main__":
    App()
