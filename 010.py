#Faça um Programa que peça a temperatura em graus Celsius
#transforme e mostre em graus Farenheit.


temperatura_celsius = int(input('Digite a temperatura em celsius: '))
temperatura_fahrenheit = int(temperatura_celsius * 9/5)+32

print(f'Temperatura em Celsius: {temperatura_celsius} °C')
print(f'Temperatura em Fahrenheit: {temperatura_fahrenheit} °F')