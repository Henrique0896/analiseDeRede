from socket import socket, AF_INET, SOCK_STREAM
from os import system
from time import sleep

class VarreduraPortas:
    def __init__(self, hostsAtivos):
        self.hostsAtivos = hostsAtivos
        self.portasAbertas = []#Vai ser preenchido se chamar varrerportas()

    def varrerPortas(self):
        try:
            print("\nDigite o intervalo de portas que vai ser coberto na varredura:")
            portaInicial = int(input("Porta Inicial: "))
            portaFinal = int(input("Porta Final: "))
            if(portaInicial > portaFinal or portaInicial < 0 or portaFinal > 65535):
                raise Exception
            system('clear')
        except:
            print('Erro! Verifique e tente novamente!')
            exit()
        for ip in self.hostsAtivos:
            try:
                portasAbertas = []
                for porta in range(portaInicial, portaFinal+1):
                    print("Varrendo o host: %s" %(ip))
                    print("Verificando porta: %d" %(porta))
                    sock = socket(AF_INET, SOCK_STREAM)
                    res = sock.connect_ex((ip,  porta))
                    system('clear')
                    if (res == 0):
                        portasAbertas.append(porta)
            except:
                print('Erro! Verifique e tente novamente')
                exit()
            print("Varredura encerrada no host: %s" %(ip))
            print("%d porta(s) aberta(s)" %(len(portasAbertas)))
            self.portasAbertas.append(portasAbertas)
            sleep(3)
            system('clear')
        self.mostrarPortasAbertas(portaInicial, portaFinal)

    def mostrarPortasAbertas(self, portaInicial, portaFinal):
        system('clear')
        print("Relatorio de Portas Abertas: ")
        print("Numéro de Portas Abertas no Intervalo %d - %d" %(portaInicial, portaFinal))
        print("        HOST                PORTAS ABERTAS  ")
        i=0
        for ip in self.hostsAtivos:
            sizePortas = len(self.portasAbertas[i])  
            print(" | %s       |          %d        | " %(ip,sizePortas))
            i+=1
        i=0
        for ip in self.hostsAtivos:
            if( len(self.portasAbertas[i]) > 0):
                print("\nLista de Portas Abertas do host: %s"%(ip))
                for porta in self.portasAbertas[i]:
                    print(porta)
                print("\n")
            i+=1