
from Rede import Rede
from Varredura import VarreduraPortas
from os import system

if __name__ == '__main__':
    system('clear')
    print("Analisando sua Rede...")
    minhaRede = Rede()
    system('clear')

    hosts = minhaRede.mostrarHostsAtivos()

    hosts = VarreduraPortas(hosts)

    hosts.varrerPortas()
