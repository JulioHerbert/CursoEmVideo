salário = float(input('Digite o valor do salário do funcionário R$: '))
if salário >= 1250:
    cal = (salário * 10)/100+salário
    print('Seu salário foi {} e com aumento de 10% ficou R$: {:.2f}'.format(salário, cal))
if salário < 1250:
    cal2 =(salário * 15)/100+salário
    print('Seu salário foi {} e com aumento de 15% ficou R$: {:.2f}'.format(salário, cal2))
