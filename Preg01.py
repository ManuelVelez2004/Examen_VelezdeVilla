"""
INTERCAMCIAR VALORES DE 2 VARIABLES
"""
#Datos de entrada:
# A: 8
# B: 9
# Datos de Salida:
# A: 9
# B: 8
def cambio_de_valores(A, B):
    a = A
    b = B
    A = b
    B = a
    print(f'Datos de salida:')
    print(f'A = {A} \nB = {B}')
print(f'Datos de entrada:')
A= 8
B= 9
print(f'A = {A}')
print(f'B = {B}')
cambio_de_valores(A, B)