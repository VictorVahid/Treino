entrada = input('Digite [M]atutino ou [V]espertino ou [N]oturno: ').lower()

if entrada == 'm':
        print('Bom Dia!')
elif entrada =='v':
        print('Boa Tarde!')
elif entrada == 'n':
        print('Boa Noite!')
else:
    print('Valor Inválido!')