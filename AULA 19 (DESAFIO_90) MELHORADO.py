aluno = dict()
aluno ['Nome'] = str(input('Digite nome do aluno: ')).strip()
aluno ['N1'] = float(input(f'Qual foi a N1 de {aluno ["Nome"]}?: '))
aluno ['N2'] = float(input(f'Qual foi a N2 de {aluno ["Nome"]}?: '))
média = (aluno ['N1'] + aluno ['N2'])/2
print('-'*40)
for n1, n2 in aluno.items():
    print(f' - {n1} do aluno: {n2}')
print(f' - Média do aluno: {média}')
if média >= 6:
    print(' - situação é igual a APROVADO!')
elif média <=3:
    print(' - situação é igual a REPROVADO...')
else:
    print(' - situação é igual a RECUPERAÇÃO...')
print('-'*40)
