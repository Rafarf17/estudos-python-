class Main:
    pass

print("teste")

from cliente import cliente
from Conta import Conta

c1= cliente("João", "11111-1101")
conta=Conta(c1.nome, 6565, 0)

print(conta.titular, "Numero: ", conta.numero, "Seu saldo: ", conta.salario)


