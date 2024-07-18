def limpiarPantalla () -> None:
    from os import system
    system('cls')

def pausa () -> None:
    from os import system
    system('pause')

def cargarAlimentos () -> list[dict]:
    lista_alimentos = []
    archivo = open('lista_alimentos.csv','r')

    llaves = archivo.readline().replace('\n','').split(';')

    datos_alimentos = archivo.readlines()
    for alimento in datos_alimentos:
        dict_alimento = {}
        datos = alimento.replace('\n','').split(';')
        for i in range(len(llaves)):
            dict_alimento.update({llaves[i]:datos[i]})
        lista_alimentos.append(dict_alimento)

    archivo.close()
    return lista_alimentos

def imprimirMenu (opcionesMenu:dict) -> str:
    for opcion in opcionesMenu.keys():
        print(str(opcion).capitalize(),'=>',opcionesMenu[opcion][0])
    selec = input('>> ')
    for lista_opciones in opcionesMenu.values():
        if (selec in lista_opciones):
            return selec
    return 'ERR-NO-SELEC'

