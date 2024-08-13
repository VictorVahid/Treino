"""
Faça um programa que peça o tamanho de um arquivo para download (em MB)
velocidade de um link de Internet (em Mbps)
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

"""


download_mb = float(input('Digite o tamanho de um arquivo para download (em MB): '))
velocidade_internet = float(input('Digite a velocidade de um link de Internet (em Mbps): '))

tempo = (download_mb * 8)/ velocidade_internet
minutos = tempo // 60
segundos = tempo % 60

print(f"{minutos:.0f} Minutos e {segundos:.0f} Segundos")



