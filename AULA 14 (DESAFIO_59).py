n1 = int(input('1º VALOR: '))
n2 = int(input('2º VALOR: '))
opção = 0
while opção != 5:
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação de {} e {} é: {}'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            print('1º foi o MAIOR')
        elif n2 > n1:
            print('2º foi o MAIOR')
        else:
            print('Valores iguais')
    elif opção == 4:
        n1 = int(input('Digite novamente o 1º VALOR: '))
        n2 = int(input('Digite novamente o 2º VALOR: '))
    elif opção == 5:
        print('Encerrando...')
print('Programa encerrado!')
