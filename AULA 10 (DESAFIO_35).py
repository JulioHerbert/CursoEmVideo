n1 = float(input('Digite o primero segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print('Segmentos PODEM FORMAR um triângulo!')
else:
    print('Segmentos NÃO PODEM FORMAR um triângulo!')

