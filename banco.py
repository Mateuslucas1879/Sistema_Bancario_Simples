from clientes import Cliente
from contas import ContaCorrente, ContaSalario, ContaPoupanca, ContaEmpresarial
import random

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = {}
        self.contas = {}

    def criar_cliente(self, nome, cpf, endereco=None, telefone=None):
        if cpf in self.clientes:
            return None
        cliente = Cliente(nome, cpf, endereco, telefone)
        self.clientes[cpf] = cliente
        return cliente

    def buscar_cliente(self, cpf):
        return self.clientes.get(cpf)

    def listar_clientes(self):
        return list(self.clientes.values())

    def _gerar_numero_conta(self):
        while True:
            numero = random.randint(10000000, 99999999)
            if numero not in self.contas:
                return numero

    def _criar_conta_generica(self, cpf, classe_conta, *args):
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            return None
        numero = self._gerar_numero_conta()
        conta = classe_conta(numero, cliente, *args)
        self.contas[numero] = conta
        cliente.adicionar_conta(conta)
        return conta

    def criar_conta_corrente(self, cpf, saldo_inicial=0, limite=500):
        return self._criar_conta_generica(cpf, ContaCorrente, saldo_inicial, limite)

    def criar_conta_poupanca(self, cpf, saldo_inicial=0):
        return self._criar_conta_generica(cpf, ContaPoupanca, saldo_inicial)

    def criar_conta_salario(self, cpf, saldo_inicial=0):
        return self._criar_conta_generica(cpf, ContaSalario, saldo_inicial)

    def criar_conta_empresarial(self, cpf, saldo_inicial=0, limite=5000):
        return self._criar_conta_generica(cpf, ContaEmpresarial, saldo_inicial, limite)

    def buscar_conta(self, numero_conta):
        return self.contas.get(numero_conta)

    def listar_contas(self):
        return sorted(self.contas.values(), key=lambda c: c.numero)

    def autenticar_cliente(self, cpf, numero_conta):
        conta = self.buscar_conta(numero_conta)
        return conta is not None and conta.cliente.cpf == cpf

    def remover_cliente(self, cpf):
        cliente = self.clientes.pop(cpf, None)
        if not cliente:
            return False
        contas_remover = [num for num, conta in self.contas.items() if conta.cliente.cpf == cpf]
        for num in contas_remover:
            del self.contas[num]
        return True

    def remover_conta(self, numero_conta):
        return self.contas.pop(numero_conta, None)
