ficha = list()
while True:
    nome = str(input('Digite nome do aluno: '))
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    conti = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if conti in 'Nn':
        break
print('PROGRAMA ENCERRADO!')
print(f'{"Núm.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Deseja ver notas de qual aluno? (999 finaliza o programa): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} é {opc[1]}')
    print('VOLTE SEMPRE!')
