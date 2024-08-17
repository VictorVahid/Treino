
dias = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']

while True:
    try:
           entrada = int(input('Digite um número: '))
           if 1 <= entrada <= 7:
                print(dias[entrada - 1])
                break
           else:
                print('Digite um valor válido!')
    except ValueError:
        print('Por favor, digite um número inteiro')
