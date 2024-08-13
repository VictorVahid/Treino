#Faça um Programa que verifique se uma letra digitada é "F" ou "M"
# Conforme a letra escrever:
#F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite [M]asculino ou [F]eminino: ')

if sexo == 'F' or sexo == 'f' :
    print('Feminino')
elif sexo == 'M' or sexo == 'm':
    print('Masculino')
else:
    print('Sexo invalido')