
salario_hora = float(input('Digite o seu sálario hora: '))
horas_trabalhadas = int(input('Digite as Horas trabalhadas no mês: '))

salario_mes = salario_hora * horas_trabalhadas

#Calculos
imposto_de_renda = salario_mes * (11 / 100)
inss = salario_mes * (8 / 100)
sindicato = salario_mes * (5 / 100)
descontos = imposto_de_renda + inss + sindicato
salario_liquido  = salario_mes - descontos

#Saidas
print(f'Salário Bruto: R${salario_mes:.2f}')
print(f'IR (11%) : R${imposto_de_renda:.2f}')
print(f'INSS (8%) : R${inss:.2f}')
print(f'Sindicato (5%) : R${sindicato:.2f} ')
print(f'Sálario Liquido: R${salario_liquido:.2f}' )
