from random import randint
jogador = int(input('Qual número?: '))
pc = randint(0, 10)
contador = 0
print(pc)
while jogador!=pc:
    print('Você errou')
    jogador = int(input('Digite outro número: '))
    contador = contador + 1
print('Vocè venceu!\nNÚMERO DIGITADO: {}\nNÚMERO PENSADO: {}\nNÚMEROS DE TENTATIVAS: {}'.format(jogador, pc, contador))
