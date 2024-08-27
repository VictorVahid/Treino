"""
    Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""

anoEntrada = input('Digite um número correspondente à um ano: ')

if len(anoEntrada) == 4:
    entradaInteira = int(anoEntrada)
    if entradaInteira % 4 == 0:
        print(f'O ano {anoEntrada} é bissexto!')
    else:
     print('Não é bissexto!')
else: 
    print('Entrada Inválida!')