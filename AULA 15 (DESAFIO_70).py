preço = soma = altocusto = menor = cont = 0
barato = ' '
while True:
    nome = conti = ' '
    nome = str(input('Qual nome do produto?: ')).strip()
    cont = cont + 1
    preço = float(input('Qual preço do produto?: '))
    print('-'*30)
    print(f'PRODUTO: {nome} PREÇO: {preço}')
    print('-'*30)
    soma = soma + preço
    if preço > 1000:
        altocusto = altocusto + 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    while conti not in 'SN':
        conti = str(input('Deseja continuar?: [S/N]')).strip().upper()[0]
    if conti == 'N':
            break
print('-'*30)
print('Total gasto na compra: R${:.2f}\nCUSTOS ACIMA DE R$1000.00: {}'.format(soma,altocusto))
print('Menor produto foi a {} e custou: R${:.2f}'.format(barato,menor))
print('-'*30)

