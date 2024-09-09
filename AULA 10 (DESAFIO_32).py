from datetime import date
ano = int(input('Escolha um ano OU escreva "0" para saber o ano do PC: '))
if ano == 0:
    ano = date.today().year
    print('Estamos atualmente em: {}'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSEXTO'.format(ano))
else:
    print('{} NÃO é BISSEXTO'.format(ano))
