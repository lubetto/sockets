import fnmatch
with open("datos.txt", "r") as datos:
    cuentas = datos.read().split('\n')
buscar = "*78454122*"
dominio = fnmatch.filter(cuentas, buscar)
strdominio = str(dominio).strip("['']")
posicion = cuentas.index(strdominio)
if strdominio in cuentas:
    print(strdominio)
    print("Esta cuenta esta en la posicion {} ".format(posicion))