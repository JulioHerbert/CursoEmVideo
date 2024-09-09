print('-'*60)
valor = int(input('Digite um valor a ser sacado R$: '))
print('-'*60)
total = valor
céd = 50
contcéd = 0
while True:
    if total >= céd:
        total -= céd
        contcéd = contcéd + 1
    else:
        if contcéd >= 1:
            print('Total de {} cédulas de R$: {}'.format(contcéd, céd))
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        contcéd = 0
        if total == 0:
            break
print('PROGRAMA ENCERRADO')
