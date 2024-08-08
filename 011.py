#Faça um Programa que peça 2 números inteiros e um número real.
#Calcule e mostre: o produto do dobro do primeiro com metade do segundo.
#a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

#Entradas
num1_inteiro = int(input('Digite um número inteiro: '))
num2_inteiro = int(input('Digite um outro número inteiro: '))
numreal  = float(input('Digite um número real: '))

#Calculos
dobro_num1 = num1_inteiro *2
metade_num2 = num2_inteiro /2
produto1 = dobro_num1 * metade_num2

triplo_num1 = num1_inteiro *3
produto2 = triplo_num1 * numreal
cubo_numreal = numreal**3

#Saida Um

print(f'Dobro do primeiro número: {dobro_num1}')
print(f'Metade do segundo número: {metade_num2}')
print(f'Produto entre eles: {produto1}\n')

# #Saida Dois

print(f'Triplo do primeiro número: {triplo_num1} ')
print(f'Produto entre eles: {produto2} ')
print(f'Cubo do número real: {cubo_numreal} ')

