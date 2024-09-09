num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
        int(input('Digite um número: ')),
         int(input('Digite um número: ')))
print(f'Você digitou os valores: {num}')
print(f'Número 9 apareceu: {num.count(9)} vezes')
if 3 in num:
    print(f'Número 3 está na {(num.index(3)+1)}º posição')
else:
    print(f'Nenhum valor 3 encontrado')
print(f'Números pares digitados: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
