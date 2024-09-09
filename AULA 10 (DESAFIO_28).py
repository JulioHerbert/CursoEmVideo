from random import randint
pc = randint(0,5)
print("==" * 30)
print('>>> TENTE ADIVINHAR UM NÚMERO ENTRE 0 E 5 <<<!')
print("==" * 30)

num1 = int(input('Digite o número!: '))
if num1 == pc:
    print('PARÁBENS VOCÊ ACERTOU!')
else:
    print('Número pensado foi {} e vocè digitou {}, VOCÈ PERDEU'.format(pc,num1))
