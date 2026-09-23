from ping3 import ping, verbose_ping

LOCAL = '192.168.0.'
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
    req = ping(f'{LOCAL}{octeto+1}', timeout=1)

    if (req != None and req != False):
        IPS.append(f'{LOCAL}{octeto+1}')

print(IPS)