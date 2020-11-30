from socket import socket, AF_INET, SOCK_DGRAM
from multiprocessing import Queue, Process
from os import devnull
from subprocess import check_call

class Rede:
    def __init__(self):
        self.meuIP = '' #vai ser preenchido por obterMeuIP() no construtor
        self.hostsAtivos = [] #vai ser preenchido por obterHostsAtivos() no construtor
        self.obterMeuIP()#obtem IP
        self.obterHostsAtivos()#Obtem hosts ativos

    def obterMeuIP(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        meuIP = sock.getsockname()[0]
        sock.close()
        self.meuIP = meuIP
    
    def baseIP(self):
        ipPart = self.meuIP.split('.')
        baseIP = ipPart[0] + '.' + ipPart[1] + '.' + ipPart[2] + '.'
        return baseIP

    def ping(self, tarefas, resultados):
        DEVNULL = open(devnull, 'w')
        while True:
            ip = tarefas.get()
            if ip is None:
                break
            try:
                check_call(['ping', '-c1', ip], stdout=DEVNULL)
                resultados.put(ip)
            except:
                pass

    def obterHostsAtivos(self, poolSize=255):
        baseIP = self.baseIP()
        tarefas = Queue()
        resultados = Queue()
        pool = [Process(target=self.ping, 
        args=(tarefas, resultados)) for i in range(poolSize)]
        for p in pool:
            p.start()
        for i in range(1, 255):
            tarefas.put(baseIP + '{0}'.format(i))
        for p in pool:
            tarefas.put(None)
        for p in pool:
            p.join()
        while not resultados.empty():
            ip = resultados.get()
            self.hostsAtivos.append(ip)
        
    

    def mostrarHostsAtivos(self):
        i=1
        print("Os seguintes hosts estão ativos na sua rede: ")
        for ip in self.hostsAtivos:
            print("%d -> %s" %(i,ip))
            i+=1
        return self.hostsAtivos
    






    