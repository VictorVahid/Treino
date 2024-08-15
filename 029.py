salario = float(input('Digite seu salario: '))

percentual_aumento = 0
valor_aumento = 0
salario_novo = 0


if salario <= 280:
    percentual_aumento = '20%'
    valor_aumento = (20/100) * salario
    salario_novo = salario + valor_aumento

    print(f'o salário antes do reajuste: R$ {salario:.0f}')
    print(f'o percentual de aumento aplicado: {percentual_aumento}')
    print(f'o valor do aumento: R$ {valor_aumento:.0f}')
    print(f'o novo salário, após o aumento: R$ {salario_novo:.0f}')
elif salario > 280 and salario<= 700:
    percentual_aumento = '15%'
    valor_aumento = (15/100) * salario
    salario_novo = salario + valor_aumento

    print(f'o salário antes do reajuste: R$ {salario:.0f}')
    print(f'o percentual de aumento aplicado: {percentual_aumento}')
    print(f'o valor do aumento: R$ {valor_aumento:.0f}')
    print(f'o novo salário, após o aumento: R$ {salario_novo:.0f}')
elif salario > 700 and salario<= 1500:
    percentual_aumento = '10%'
    valor_aumento = (10/100) * salario
    salario_novo = salario + valor_aumento

    print(f'o salário antes do reajuste: R$ {salario:.0f}')
    print(f'o percentual de aumento aplicado: {percentual_aumento}')
    print(f'o valor do aumento: R$ {valor_aumento:.0f}')
    print(f'o novo salário, após o aumento: R$ {salario_novo:.0f}')
elif salario > 1500:
    percentual_aumento = '5%'
    valor_aumento = (5/100) * salario
    salario_novo = salario + valor_aumento

    print(f'o salário antes do reajuste: R$ {salario:.0f}')
    print(f'o percentual de aumento aplicado: {percentual_aumento}')
    print(f'o valor do aumento: R$ {valor_aumento:.0f}')
    print(f'o novo salário, após o aumento: R$ {salario_novo:.0f}')
else:
    print('Entrada inválida!')