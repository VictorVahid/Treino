nota_um = float(input('Digite sua nota parcial: '))
nota_dois = float(input('Digite sua nota parcial 2: '))

media = float(nota_um + nota_dois / 2)

if media >= 7:
    print(f'Media {media} Aprovado')
elif media < 7:
    print(f'Media {media} Reprovado')
elif media == 10 :
    print(f'Media {media} Aprovado com distinção')
else:
    print('Entrada invalida!')