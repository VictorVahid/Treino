#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.


salario_hora = float(input('Digite seu salário hora: '))
horas_trabalhadas = float(input('Digite horas trabalhadas no mês: '))


salario_total = horas_trabalhadas * salario_hora

print(f'Salário total do mês é: R${salario_total:.2f}')
