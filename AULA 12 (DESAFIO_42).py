n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    if n1 == n2 and n2 == n3 and n3 == n1:
        print('Os segmentos PODEM FORMAR um EQUILÁTERO!')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('Os segmentos PODEM FORMAR um ISÓSCELES!')
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print('Os segmentos PODEM FORMAR um ESCALENO!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo...')
    


