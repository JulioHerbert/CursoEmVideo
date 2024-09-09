n1 = float(input('Digite a distância da sua viagem: '))
pre = (n1*0.5)
pre1 = (n1*0.45)
if n1 <= 200:
    print('Preço para sua viagem de {}Km/h foi de R$: {:.2f}'.format(n1, pre))
else:
    print('Preço para sua viagem mais longa foi de R$: {:.2f}'.format(pre1))
    
    
