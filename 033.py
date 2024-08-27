def eh_triangulo(lado_a, lado_b, lado_c):
  """Verifica se três lados formam um triângulo."""
  return (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a)

def classifica_triangulo(lado_a, lado_b, lado_c):
  """Classifica um triângulo como equilátero, isósceles ou escaleno."""
  if lado_a == lado_b == lado_c:
    return "equilátero"
  elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    return "isósceles"
  else:
    return "escaleno"


lado_a = float(input('Digite o valor de um lado: '))
lado_b = float(input('Digite o valor de um lado: '))
lado_c = float(input('Digite o valor de um lado: '))


if eh_triangulo(lado_a, lado_b, lado_c):
  tipo_triangulo = classifica_triangulo(lado_a, lado_b, lado_c)
  print(f"É um triângulo {tipo_triangulo}!")
else:
  print("Os lados não formam um triângulo.")