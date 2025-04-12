try:
    Dividir = 10/0
    print(Dividir)
except ZeroDivisionError:
    print("Ha ocurrido un error, no puede dividir por cero")