num1 = int(input('Digite um número: '))
tot = 0
for c in range(1, num1+1):
    if num1 % c ==0:
        tot += 1
print('Número {} foi divisivel {} vezes'.format(num1, tot))
if tot == 2:
    print('Logo ele é primo!')
else:
    print('Ele NÃO é um número primo')
