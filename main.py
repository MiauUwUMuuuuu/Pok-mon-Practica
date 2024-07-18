from libreria_pokemon import *
import acciones_pokemon as accion
import herramientas

"""
    AGREGAR:
    ✔ loadPkm
    - menu para hacer cosas con el pkm
    - iniciar programa (?)
    - crear pokemon segun entrada de usuario
    ✔ verificar si la especia de un pokemon existe <- tendran que de alguna forma escribir las 1000+ especies (o buscar la lista lista en algun lado)
"""

#inicar el programa
# 1. revisar si hay archivos de pkm en la carpeta
    # 1.1. si hay, cargar los datos
    # 1.2. si NO hay, hacer que el usuario cree un pkm y guardarlo


mi_pokemon = {}
lista_pokemon = initPrograma()

opciones_menu = {
    'cargar' : ['l','load'],
    'accion' : ['a','accion'],
    'crear' : ['c','crear'],
    'guardar' : ['g','guardar'],
}

while (True):
    herramientas.pausa()
    herramientas.limpiarPantalla()

    print('--')
    if (mi_pokemon != {}):
        imprimirPkm(mi_pokemon)
    else:
        print('seleccionar pokemon!')
    print('--')

    selec = herramientas.imprimirMenu(opciones_menu)

    if (selec == 'ERR-NO-SELEC'):
        print('comando no valido')

    if (selec in opciones_menu['accion']):
        lista_acciones = accion.menu_acciones
        sel = herramientas.imprimirMenu(lista_acciones)
        

    if (selec in opciones_menu['cargar']):
        for i,pkm in enumerate(lista_pokemon):
            print(i+1, pkm['nombre'], pkm['especie'])

        sel = int(input('>> '))-1
        mi_pokemon = lista_pokemon[sel]
        

    if (selec in opciones_menu['crear']):
        nombre = input('ingrese nombre: ')
        especie = input('ingrese especie: ')
        nuevo_pkm = crearPkm(nombre,especie)
        imprimirPkm(nuevo_pkm)
        print('quiere establecer este como su pokemon principal? ')
        sel = input('si / no').lower()
        if (sel == 'si'):
            mi_pokemon = nuevo_pkm
        else:
            continue

    if (selec in opciones_menu['guardar']):
        savePkm(mi_pokemon)
        print('pokemon guardado')
        
    



