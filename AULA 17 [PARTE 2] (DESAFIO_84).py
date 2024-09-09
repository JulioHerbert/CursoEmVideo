pessoas = list()
dados = list()
contp = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso: ')))
    contp = contp + 1
    conti = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    pessoas.append(dados[:])
    dados.clear()
    if conti in 'Nn':
        break
for p in pessoas:
    if p[1] >= 100:
        print(f'{p[1]} está acima do peso!')
    else:
        print(f'\n{p[0]} não está acima do peso.')
print(f'Pessoas cadastradas: {contp}')
