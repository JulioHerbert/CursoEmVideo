from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    dis = ' '
    dis = str(input('Par ou ÍMPAR? [P/I]')).strip().upper()[0]
    while dis not in 'PI':
        dis = str(input('Par ou ÍMPAR? [P/I]')).strip().upper()[0]
    pc = randint(0, 10)
    soma = jogador + pc
    print(f'Jogador: {jogador}\nPC: {pc}\nTOTAL: {soma}')
    if soma % 2 == 0:
        print('DEU PAR!')
        if dis == 'P':
            print('JOGADOR VENCEU!')
            v = v + 1
        else:
            print('JOGADOR PERDEU...!')
            break
    if soma % 2 == 1:
        print('DEU ÍMPAR!')
        if dis == 'I':
            print('JOGADOR VENCEU!')
            v = v + 1
        else:
            print('JOGADOR PERDEU...!')
            break
print(f'PROGRAMA ENCERRADO!\nTOTAL DE VÍTORIAS: {v}')
    
