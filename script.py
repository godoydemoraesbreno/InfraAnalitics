from ping3 import ping, verbose_ping
from concurrent.futures import ThreadPoolExecutor
from database.banco import criar_tabela
import sqlite3

# constante de ip privado
LOCAL = '192.168.0.'

# funcao para obter o tanto de ip que sera analisado
def obter_alvos():
    IPS = []
    limite = 0

    while (limite > 254 or limite < 1):
        try:
            print("Digite um numero entre 1 e 254!")
            limite = int(input('Quantos ips deseja varrer?: '))
        except ValueError:
            print('Digite numeros!')
            print("")

    for octeto in range(limite):
        ip = f'{LOCAL}{octeto+1}'
        IPS.append(ip)

    return IPS

# funcao que verifica se o ip responde (um ip)
def varredura(ip):
        req = ping(ip)

        if (req != None and req != False):
            return ip
        else: 
            return None

# funcao que utiliza a lista de ips range e a funcao de varredura para gerar os ips que respondem
def gerar_lista_ativos(IPS):
    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(varredura, IPS))
        ips_onlines = [ip for ip in resultados if ip is not None]
    return ips_onlines

# chamadas das funcoes
alvos = obter_alvos()
ips_gerados = gerar_lista_ativos(alvos)

# funcao de insercao no banco
def insercao_de_dados():
    criar_tabela()

    conexao = sqlite3.connect("./database/banco.db")
    cursor = conexao.cursor()

    for ip in ips_gerados:
        cursor.execute("INSERT INTO historico_redes (ip, status) VALUES (?,?)", (ip, "Online"))

    conexao.commit()
    conexao.close()

# insere os dados
insercao_de_dados()
