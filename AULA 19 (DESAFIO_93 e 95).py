dic = dict()
lista = list()
time = list()
while True:
    dic.clear()
    dic ['nome'] = str(input('Digite nome do jogador: ')).strip()
    tot = int(input(f'Digite o total de partidas de {dic ['nome']}: '))
    lista.clear()
    for c in range(0, tot):
        lista.append(int(input(f'Quantos gols na partida {c+1}º? ')))
    dic ['gols'] = lista[:]
    dic ['total'] = sum(lista)
    time.append(dic.copy())
    while True:
        conti = str(input('Quer continuar? [S/N] ')).upper()[0]
        if conti in 'SN':
            break
        print(f'ERRO! Por favor responda somente [S] ou [N].')
    if conti == 'N':
        break
print('-='*30)
print('info ', end='')
for i in dic.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for temp, temp1 in enumerate(time):
    print(f'{temp:>4} ', end='')
    for temp2 in temp1.values():
        print(f'{str(temp2):<15}', end='')
    print()
print('-'*60)
while True:
    busca = int(input('Deseja fazer o levantamento de qual jogador?: [999]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! JOGADOR NÃO ENCONTRADO código {busca}! ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' na {i+1}º partidas esse jogador realizou {g} gols. ')
        print('-' * 40)
print('PROGRAMA ENCERRADO!')
        
