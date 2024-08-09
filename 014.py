
peso = float(input('Digite o peso do peixe: '))

if(peso > 50):
    excesso = peso - 50
    multa = excesso * 4

    print (f'Total do excesso: {excesso:.2f} ')
    print (f'Total de multa: {multa:.2f}')
else:
    print('Não teve excesso!')
