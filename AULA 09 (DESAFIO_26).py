n1 = str(input('Digite uma frase: ')).strip().upper()
print('Letra A apareceu: {} vezes'.format(n1.count('A')))
print('Letra A apareceu na posição: {}'.format(n1.find('A')+1))
print('Letra A apareceu pela última vez na posição: {}'.format(n1.rfind('A')+1))

