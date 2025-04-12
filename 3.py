diccionario={"nombre":"Gabriel","cargo":"Profesor"}
try:
    print(diccionario["edad"])
except KeyError:
    print("Ha ocurrido un error, la entrada ingresada no existe")