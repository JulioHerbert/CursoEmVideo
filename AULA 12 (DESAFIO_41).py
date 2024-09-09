import datetime
ano = int(input('Digite seu ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - ano
print('Você nasceu no ano {} logo tem {} anos em {}'.format(ano,idade,atual))
if idade <= 9:
    print('Você tem {} anos logo sua classificação é: MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos logo sua classificação é: INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos logo sua classificação é: JUNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos logo sua classificação é: SêNIOR'.format(idade))
elif idade > 25:
    print('Você tem {} anos logo sua classificação é: MASTER!'.format(idade))
