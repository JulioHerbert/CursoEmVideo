import random
nom1 = input('Digite o nome do primeiro aluno: ')
nom2 = input('Digite o nome do segundo aluno: ')
nom3 = input('Digite o nome do terceiro aluno: ')
nom4 = input('Digite o nome do quarto aluno: ')
nom5 = input('Digite o nome do quinto aluno: ')

nom = (nom1, nom2, nom3, nom4, nom5)

sort = random.choice(nom)

print('Aluno sorteado: {}'.format(sort))
