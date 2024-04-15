def cochera(horas):
    pagar = 6
    if horas <= 6:
        return pagar
    else:
        costo_extra = 2 * (horas - 4)
        total = pagar + costo_extra
        return total


while True:
    try:
        horas = float(input("Ingrese horas: "))
        if horas >= 0:
            break
        else:
            print("Por favor, ingrese un número positivo.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Calcular la donación
total = cochera(horas)
print("Importe a pagar s/. ", total)
