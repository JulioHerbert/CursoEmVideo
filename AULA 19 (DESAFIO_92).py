dic = dict()
from datetime import datetime
while True:
    dic ['Nome'] = str(input('Nome: ')).strip()
    nasc = int(input('Digite seu ano de nascimento: '))
    dic ['Idade'] = datetime.now().year - nasc
    dic ['Carteira'] = int(input('Carteira de Trabalho caso não tenha digite (0): '))
    if dic ['Carteira'] == 0:
        break
    dic ['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dic ['Salário'] = float(input('Salário: R$'))
    dic ['Aposentadoria'] = dic ['Idade'] + ((dic ['Ano de Contratação'] + 35) - datetime.now().year)
    break
print('-='*30)
for n1, n2 in dic.items():
    print(f' - {n1} tem o valor {n2}')
