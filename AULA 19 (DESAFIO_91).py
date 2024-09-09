from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
           'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
cont = 1
print('Valores sorteados:')
print('-'*40)
for temp1, temp2 in jogadores.items():
    print(f'{temp1} tirou {temp2} no sorteio!')
    sleep(0.4)
print('-'*40)
lista = list()
for i in sorted(jogadores, key = jogadores.get, reverse=True):
    print(f'{cont}º lugar: {i} com {jogadores[i]}')
    cont = cont + 1

