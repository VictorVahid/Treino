#Faça um Programa que peça a temperatura em graus Farenheit
#transforme e mostre a temperatura em graus Celsius.

temperatura_farenheit = int(input('Digite a temperatura em Farenheit: '))
temperatura_celsius = int(5 * (temperatura_farenheit-32) / 9)

print(f'Temperaura em Farenheit: {temperatura_farenheit} °F')
print(f'Temperatura em Celsius: {temperatura_celsius} ºC')