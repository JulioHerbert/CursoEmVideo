import math
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Nota: {:.1f} Situação: REPROVADO!'.format(m))
elif m >= 5.0 and m < 7:
    print('Nota: {:.1f} Situação: RECUPERAÇÃO!'.format(m))
elif m >= 7.0:
    print('Nota: {:.1f} Situação: APROVADO!'.format(m))
