from clientes import Cliente
from contas import ContaCorrente,ContaSalario,ContaPoupanca,ContaEmpresarial

class Banco:
    def __init__(self,nome):
        self.nome = nome
        self.clientes = {}
        self.contas = {}
        self.proximo_numero_conta = 1

    def criar_cliente(self,nome,cpf,endereco=None,telefone=None):
        if cpf in self.clientes:
            return False
        cliente = Cliente(nome,cpf,endereco, telefone)
        self.clientes[cpf] = cliente
        return cliente

    def buscar_cliente(self,cpf):
        return self.clientes.get(cpf)

    def listar_clientes(self,cpf):
        return list(self.clientes.values())


    def gerar_numero_conta(self):
        numero = self.proximo_numero_conta
        self.proximo_numero_conta += 1
        return numero

    def criar_conta_corrente(self,cpf,saldo_inicial=0,limite=500):
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            return None
        conta = ContaCorrente(self.gerar_numero_conta(),cliente,saldo_inicial,limite)
        self.contas[conta.numero] = conta
        cliente.adicionar_conta(conta)
        return conta

    def criar_conta_poupanca(self, cpf, saldo_inicial=0):
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            return None
        conta = ContaPoupanca(self._gerar_numero_conta(), cliente, saldo_inicial)
        self.contas[conta.numero] = conta
        cliente.adicionar_conta(conta)
        return conta

    def criar_conta_salario(self, cpf, saldo_inicial=0):
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            return None
        conta = ContaSalario(self._gerar_numero_conta(), cliente, saldo_inicial)
        self.contas[conta.numero] = conta
        cliente.adicionar_conta(conta)
        return conta

    def criar_conta_empresarial(self, cpf, saldo_inicial=0, limite=5000):
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            return None
        conta = ContaEmpresarial(self._gerar_numero_conta(), cliente, saldo_inicial, limite)
        self.contas[conta.numero] = conta
        cliente.adicionar_conta(conta)
        return conta

    def buscar_conta(self, numero):
        return self.contas.get(numero)

    def listar_contas(self):
        return list(self.contas.values())

