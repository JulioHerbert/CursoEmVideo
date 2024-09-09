aluno = dict()
lista = list()
aluno ['Nome'] = str(input('Digite nome do aluno: ')).strip()
aluno ['Média'] = float(input('Qual foi sua média?: '))
lista.append(aluno.copy())
print('-'*30)
for temp1 in lista:
    for n1, n2 in temp1.items():
        print(f' - {n1} igual a {n2}')
if aluno ['Média'] >= 7:
    print(f' - situação é igual a Aprovado!')
elif aluno ['Média'] < 5:
    print(f' - situação é igual a Reprovado...')
else:
    print(f' - situação é igual a Recuperação.')
print('-'*30)
    
        
    
