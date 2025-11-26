class Cliente:
    def __init__(self, nome, cpf, endereco=None, telefone=None):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.contas = []

    def adicionar_conta(self,conta):
        self.contas.append(conta)
    def atualizar_telefone(self,novo_telefone):
        self.telefone = novo_telefone
    def listar_contas(self):
        return self.contas
    def __str__(self):
        return (
            f"Cliente: {self.nome} | CPF: {self.cpf} | "
            f"Telefone: {self.telefone} | Endereço: {self.endereco}"
        )