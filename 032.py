nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))

media = (nota_1 + nota_2) / 2

media_aproveitamento = ""
resultado = ""

if media >= 9 and media <= 10:
    media_aproveitamento = "Conceito Entre 9.0 e 10.0 (A)"
    resultado = "Aprovado"
elif media >= 7.5 and media < 9:
    media_aproveitamento = "Conceito Entre 7.5 e 9.0 (B)"
    resultado = "Aprovado"
elif media >= 6 and media < 7.5:
    media_aproveitamento = "Conceito Entre 6.0 e 7.5 (C)"
    resultado = "Aprovado"
elif media >= 4 and media < 6:
    media_aproveitamento = "Conceito Entre 4.0 e 6.0 (D)"
    resultado = "Reprovado"
elif media < 4:
    media_aproveitamento = "Conceito Entre 4.0 e zero (E)"
    resultado = "Reprovado"
else:
    print("Entrada invalida!")


print(f"As notas foram: {nota_1} & {nota_2}")
print(f"{media_aproveitamento}")
print(f"{resultado}")
