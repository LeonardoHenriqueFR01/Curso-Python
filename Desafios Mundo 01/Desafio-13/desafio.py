# Reajuste salarial

salario = float(input('Qual é o salário do funcionário: R$'))

novo_salario = salario + (salario / 100 * 15)

print(f'Um que funcionário que ganhava R${salario}, com um aumento de 15%, passa a receber R${novo_salario:.2f}')
