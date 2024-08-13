
#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


try:
    entrada = int(input('Digite um valor inteiro: '))
    if entrada < 0: 
        print(f'{entrada} é negativo')
    else:
        print(f'{entrada} é positivo')
except:
    print('Digite um valor inteiro válido!')