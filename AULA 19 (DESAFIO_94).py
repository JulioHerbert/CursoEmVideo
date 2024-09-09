pessoas = dict()
lista = list()
cont = soma = media = temp1 = temp2 = 0
while True:
    pessoas ['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas ['sexo'] = str(input('Sexo: [M/F] ')).strip()
        if pessoas ['sexo'] in 'MmFf':
            break
        print(f'ERRO! Por favor digite SOMENTE [M] ou [F].')
    pessoas ['Idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    cont = cont + 1
    soma = soma + pessoas['Idade']
    while True:
        conti = str(input('Quer continuar? [S/N] '))
        if conti in 'SsNn':
            break
        print(f'ERRO! no programa responda SOMENTE [S] ou [N].')
    if conti in 'Nn':
        break
print(f'-='*40)
print(f'Total de pessoas cadastradas: {cont}')
media = soma / len(lista)
print('-='*40)
print(f'A média da idade é: {media:.2f}')
print('-='*40)
print(f'Mulheres cadastradas:')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{temp1+1}º {p["nome"]}')
        temp1 = temp1 + 1
print('-='*40)
print(f'Lista com nomes das pessoas acima da média de idade:')
for p in lista:
    if p['Idade'] >= media:
        print(f'{temp2+1}º {p["nome"]}')
        temp2 = temp2 + 1
