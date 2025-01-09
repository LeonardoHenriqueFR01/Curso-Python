# Seno, Cosseno e Tangente

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))

rad = radians(angulo)

seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f'O ângulo de {angulo:.1f}° tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo:.1f}° tem o SENO de {cosseno:.2f}')
print(f'O ângulo de {angulo:.1f}° tem o SENO de {tangente:.2f}')
