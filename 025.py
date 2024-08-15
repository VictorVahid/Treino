numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))

maior = max(numero_1,numero_2,numero_3)
menor = min(numero_1,numero_2,numero_3)

print(f'O menor número é o {menor:.0f}')
print(f'O maior número é o {maior:.0f}')