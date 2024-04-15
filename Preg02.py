"""
DADO n, hallar la suma de los n primeros numeros naturales.
"""
#Datos de entrada:
# n : 100
# Datos de Salida:
# Sumatoria = 5050
def n_suma_primeros(n):
    i = (n * (n-1)) / 2
    print(f'Datos de Salida: \nSumatoria = 5050')
n = 100
print(f'Datos de entrada: \nn: {n}')
n_suma_primeros(n)