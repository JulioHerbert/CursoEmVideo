cont = menor = valor = 0

while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    valor = int(input('Digite o valor do produto: '))
    cont = cont + 1
    print(f'NOME: {nome} VALOR: {valor}')
    if cont == 1:
        menor = valor
    else:
        if valor < menor:
            menor = valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja parar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f'FIM!\nMENOR VALOR: {menor}')
