import random
import time

itens = ('Pedra','Papel','Tesoura')
pc = random.randint(0, 2)
n1 = int(input('ESCOLHA UMA OÇÃO:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nSELECIONE SUA JOGADA: '))
print('JO')
time.sleep(1.5)
print('KEN')
time.sleep(1.5)
print('GUNNN!')
print('Computador jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[n1]))
if pc == 0:
    if n1 == 0:
        print('EMPATE')
    elif n1 == 1:
        print('JOGADOR VENCEU!')
    elif n1 == 2:
        print('JOGADOR PERDEU!')
    else:
        print('JOGADA FORA DE REQUISIÇÃO')
elif pc == 1:
    if n1 == 0:
        print('COMPUTADOR VENCEU!')
    elif n1 == 1:
        print('EMPATE!')
    elif n1 == 2:
        print('COMPUTADOR PERDEU!')
    else:
        print('JOGADA FORA DE REQUISIÇÃO')
elif pc == 2:
    if n1 == 0:
        print('COMPUTADOR PERDEU!')
    elif n1 == 1:
        print('COMPUTADOR VENCEU!')
    elif n1 == 2:
        print('EMPATE')
    else:
        print('JOGADA FORA DE REQUISIÇÃO')
