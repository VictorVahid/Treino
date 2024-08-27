dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês : '))
ano = int(input('Digite o ano: '))

if ano < 0:
    print('Ano inválido!')
else:
    if mes < 1 or mes > 12:
        print('Mês inválido!')
    elif mes in [1 ,3, 5, 7, 8, 10, 12]:
        if dia > 0 and dia <32:
            print('Data válida!')
        else: 
            print('Dia inválido!')
    elif mes in [4, 6, 9, 11]:
        if dia > 0 and dia <31: 
            print('Data válida!')
        else: 
            print('Dia inválido!')
    else:
        if ano % 4 == 0: 
            if dia > 0 and dia < 30: 
                print('Data valida!')
            else: 
                print('Data inválida!')
        else:
            if dia > 0 and dia < 29:
                print('Data válida!')
            else: 
                print('Dia inválido!')