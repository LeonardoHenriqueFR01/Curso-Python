# TODOS OS NÚMEROS PARES DE 2 ATÉ 50 

from time import sleep

print('-=' * 12)
print('\033[0;33mNÚMEROS PARES DE 2 A 50\033[m')
print('-=' * 12)

for c in range(2, 51, 2):
    print(c)
    sleep(0.5)
