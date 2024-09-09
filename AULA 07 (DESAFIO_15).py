dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de Km percorridos: '))
cal = (dias * 60)+(km * 0.15)
print('Valor total a ser pago é R${:.2f}'.format(cal))

