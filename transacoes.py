from datetime import datetime

class Transacoes:
    def __init__(self):
        self.extrato = []

    def registrar(self,tipo,valor,origem=None,destino=None):
        registro = {
            "tipo": tipo,
            "valor": valor,
            "origem": origem,
            "destino": destino,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        self.extrato.append(registro)

    def depositar(self,conta,valor):
        if valor <= 0:
            return False
        conta.depositar(valor)
        self.registrar("DEPOSITO",valor,destino=conta.numero)
        return True

    def sacar(self,conta,valor):
        if conta.sacar(valor):
            self.registrar("SAQUE",valor,origem=conta.numero)
            return True
        return False

    def transferir(self,conta_origem,conta_destino,valor):
        if valor <= 0:
            return False
        if not conta_origem.sacar(valor):
            return False
        conta_destino.depositar(valor)
        self.registrar("TRANSFERENCIA",valor,origem=conta_origem.numero,destino=conta_destino.numero)
        return True

    def listar_extrato(self):
        return self.extrato

