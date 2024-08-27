def calcula_raizes(a, b, c):

    if a == 0:
        return "A equação não é do segundo grau."

    delta = b**2 - 4*a*c

    if delta < 0:
        return "A equação não possui raízes reais, pois o discriminante (delta) é negativo."
    elif delta == 0:
        raiz = -b / (2*a)
        return f"A equação possui uma raiz real: {raiz}"
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        return f"A equação possui duas raízes reais distintas: {raiz1:.2f} e {raiz2:.2f}"

# Entrada do usuário
valorA = float(input('Digite o valor de A: '))

if valorA != 0:
    valorB = float(input("Digite o valor de b: "))
    valorC = float(input("Digite o valor de c: "))
    resultado = calcula_raizes(valorA, valorB, valorC)
    print(resultado)
else:
    print("A equação não é do segundo grau.")