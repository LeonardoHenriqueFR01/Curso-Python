# Cadrastro de pessoas 


print('\033[33m-\033[m' * 40)
print(f'{"CADASTRE UMA PESSOA":^40}')
print('\033[33m-\033[m' * 40)

tot_18 = tot_mulher_20 = tot_homens = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    res = str(input('Deseja continuar [S/N]: ')).upper()
    if idade >= 18:
        tot_18 += 1
    if sexo == 'F' and idade < 20:
        tot_mulher_20 += 1
    if sexo == 'M':
        tot_homens += 1
    if res == 'S':
        continue
    else:
        break




print(f'Total de pessoas com mais de 18 anos: {tot_18}!')
print(f'Ao todo temos {tot_homens} homens cadrastrasdos!')
print(f'E temos {tot_mulher_20} mulheres com menos de 20 anos!')
