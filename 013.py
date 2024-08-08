#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7



altura = float(input('Digite sua altura: '))
sexo  = input('Digite seu sexo: [H]omem ou  [M]ulher: ')

peso = 0.0
peso_ideal = 0.0

if ('H' in  sexo):
  peso_ideal =  (72.7 * altura) - 58 
  print(f'O peso ideal é {peso_ideal:.2f}')
elif('M' in sexo ):
  peso_ideal = (62.1 * altura) - 44.7 
  print(f'O peso ideal é {peso_ideal:.2f}')
else:
  print('Entrada Invalida!')


