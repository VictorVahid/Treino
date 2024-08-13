
#Faça um Programa que peça dois números e imprima o maior deles.
try: 
    entrada = int(input('Digite o primeiro número: '))
    entrada_2 = int(input('Digite o segundo número: '))

    if(entrada > entrada_2):
            print(f'{entrada} > {entrada_2}')
    elif(entrada_2 > entrada):
         print(f'{entrada_2} > {entrada}')
    else:
            print(f'{entrada} = {entrada_2}')
except:
     print('Digite um número inteiro válido!')
