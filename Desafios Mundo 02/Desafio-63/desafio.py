# Sequência de fibonacci 


print('=' * 40)
print(f'{"Sequencia de fibonacci":^40}')
print('=' * 40)

ter = int(input('Quantos termos você quer mostrar: '))

t1 = 0
t2 = 1
print('~' * 40)
print(f'{t1} - {t2}', end='')
cont = 3

while cont <= ter:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')
