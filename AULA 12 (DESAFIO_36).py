vcasa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o salário do comprador: R$'))
anos = int(input('Em quantos anos você vai pagar: '))
pre = vcasa / (anos * 12)
por = (sal * 30) / 100
if pre >= por:
    print('Seu empréstime de {:.2f}R$ foi NEGADO'.format(pre))
else:
    print('Seu empréstime de {:.2f}R$ foi PERMITIDO'.format(pre))

