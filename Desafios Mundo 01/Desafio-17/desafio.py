# Catetos e Hipotenusa

# Fazendo manualmente
cateto_oposto = float(input('Cumprimento do cateto oposto: '))
cateto_adjacente = float(input('Cumprimento do cateto adjacente: '))

hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** 0.5

print(f'A hipotenusa vai medir {hipotenusa:.2f}')


# Usando biblioteca

from math import hypot

cateto_opo = float(input('Cumprimento do cateto oposto: '))
cateto_ad = float(input('Cumprimento do cateto adjacente: '))

hipote = hypot(cateto_ad, cateto_opo)

print(f'A hipotenusa vai medir {hipote:.2f}')
