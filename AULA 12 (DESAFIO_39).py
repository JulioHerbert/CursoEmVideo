import datetime
ano = int(input('Digite seu ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))
if idade == 18:
    print('Você precisa comparecer a junta militar IMEDIATAMENTE!')
elif idade > 18:
    idade1 = idade - 18
    print('Você já deveria ter se alistado a cerca de {} anos'.format(idade1))
    ano1 = atual - idade1
    print('Seu alistamento foi em {}'.format(ano1))
elif idade < 18:
    idade1 = 18 - idade
    print('Ainda faltam {} anos para seu alistamento'.format(idade1))
    ano1 = atual + idade1
    print('Ainda faltam {} anos para seu alistamento'.format(ano1))

    
