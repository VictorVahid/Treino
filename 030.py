valor_hora = float(input("Digite seu valor Hora: "))
qtd_horas_mes = float(input("Digite quantas horas foram trabalhadas no Mês: "))

# Declaracao de variaveis
texto_imposto_renda = " "
valor_imposto_renda = 0.0
salario_bruto = valor_hora * qtd_horas_mes
imposto_renda = 0.0
salario_liquido = 0.0

# Descontos Imposto de renda
if salario_bruto <= 900:
    texto_imposto_renda = "isento"
    valor_imposto_renda = 0.0
elif salario_bruto > 900 and salario_bruto <= 1500:
    texto_imposto_renda = "Desconto de 5%"
    valor_imposto_renda = 0.05
    imposto_renda = valor_imposto_renda * salario_bruto
elif salario_bruto > 1500 and salario_bruto <= 2500:
    texto_imposto_renda = "Desconto de 10%"
    valor_imposto_renda = 0.1
    imposto_renda = valor_imposto_renda * salario_bruto
elif salario_bruto > 2500:
    texto_imposto_renda = "Desconto de 20%"
    valor_imposto_renda = 0.2
    imposto_renda = valor_imposto_renda * salario_bruto
else:
    print("Entrada inválida!")

# Descontos INSS
inss = (10 / 100) * salario_bruto

# FGTS
fgts = (11 / 100) * salario_bruto

# Descontos totais
total_descontos = imposto_renda + inss

# Salario Liquido
salario_liquido = salario_bruto - total_descontos

# Saidas
print(
    f"\nSalário Bruto     : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)       : R${imposto_renda:.2f}",
    f"\n(-) INSS ( 10%)   : R${inss:.2f}",
    f"\nFGTS (11%)        : R${fgts:.2f}",
    f"\nTotal de descontos: R${total_descontos:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
)
