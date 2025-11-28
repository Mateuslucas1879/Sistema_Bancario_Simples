class Conta:
    def __init__(self, numero,cliente,saldo_inicial=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo_inicial

    def depositar(self,valor):
        if valor <= 0:
            return False
        self.saldo += valor
        return True
    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        return True

    def __str__(self):
        return f"Conta {self.numero} | Cliente: {self.cliente.nome} | Saldo: {self.saldo}"


class ContaCorrente(Conta):
    def __init__(self,numero,cliente,saldo_inicial=0,limite = 500):
        super().__init__(numero,cliente,saldo_inicial)
        self.limite = limite

    def sacar(self, valor):
        if valor <= 0:
            False
        self.saldo -= valor
        return True



class ContaPoupanca(Conta):
    def aplicar_rendimento(self,taxa):
        if taxa <= 0:
            return False
        rendimento =self.saldo * taxa
        self.saldo += rendimento
        return True

class ContaSalario(Conta):
    def __init__(self,numero,cliente,saldo_inicial=0):
        super().__init__(numero,cliente,saldo_inicial)

    def sacar(self, valor):
        if valor <= 0:
            False
        self.saldo -= valor
        return True


class ContaEmpresarial(Conta):
    def __init__(self,numero,cliente,saldo_inicial=0,limite=500):
        super().__init__(numero, cliente, saldo_inicial,)
        self.limite = limite

    def sacar(self, valor):
        if valor <= 0:
            return False
        if valor > self.saldo + self.limite:
            return False
        self.saldo -= valor
        return True
