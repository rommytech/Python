def dividir(p1, p2):
    try:
        resultado = p1 / p2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        resultado = 0
    return resultado
