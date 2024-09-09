num = list()
conti = 'SsNn'
while True:
    n2 = int(input('Digite um valor: '))
    if n2 not in num:
        num.append(n2)
        print('ADD com sucesso!')
    else:
        print('Valor invalido.')
    conti = str(input('Quer continuar? [S/N]')).strip()[0]
    if conti in 'Nn':
        break
print(f'Números adicionados: {num}')
