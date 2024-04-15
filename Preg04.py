def Donacion(ganancia):
    if ganancia > 0 and ganancia <= 1000:
        return ganancia * (5 / 100)
    if ganancia > 1000 and ganancia <= 1500:
        return ganancia * (7 / 100)
    if ganancia > 1500 and ganancia <= 2000:
        return ganancia * (8 / 100)
    if ganancia > 2000 and ganancia <= 5000:
        return ganancia * (10 / 100)
    if ganancia > 5000:
        return ganancia * (15 / 100)

while True:
    try:
        ganancia = float(input("Ingrese la ganancia: "))
        if ganancia >= 0:
            break
        else:
            print("Por favor, ingrese un número positivo.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Calcular la donación
donacion = Donacion(ganancia)
print("La donación s/. ", donacion)