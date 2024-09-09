from random import randint
tupla = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
cont = 1
for c in tupla:
    while True:
        print(f'{cont}º número sorteado: {c}')
        cont += 1
        break
print(f'Maior número foi: {max(tupla)}')
print(f'Menor número foi: {min(tupla)}')


