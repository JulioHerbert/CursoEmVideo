vel = float(input('Qual sua velocidade em Km/h?: '))
pre = (vel-80)*7
if vel > 80:
    print('MULTADO!, Você ultrapassou o limite de velocidade!')
    print('Você está dirigindo a {:.2f} KM/h, logo sua multa vai ser: {:.2f}'.format(vel, pre))
else:
    print('Você está dirigindo com segurança!')
