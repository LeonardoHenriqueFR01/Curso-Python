# NÚMERO POR EXTENÇO 


cont = ('Zero', 'Um', 'Dois', 'três', 'Quatro', 'Cinco', 
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
        'Doze', 'Treze', 'catorze', 'Quinze', 'Dezesseis', 
        'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {cont[num]}!')
