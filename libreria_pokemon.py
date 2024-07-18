def crearPkm (nombre:str,especie:str) -> dict:
    pkm = {
        'nombre':nombre,
        'hambre':'50',
        'felicidad':'50'
    }

    pkm.update(getPokemonInfoByEspecie(especie))

    return pkm

def savePkm (pkm:dict) -> None:
    nombre_archivo = str(pkm['nombre'])+'_'+str(pkm['especie'])+'_datos.pkm'
    archivo = open(nombre_archivo, 'w')
    for v in pkm.values():
        archivo.write(str(v)+'\n')
    archivo.close()

def loadPkm (nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo,'r')
    #revisar que archivo exista

    datos_pkm = archivo.readlines()

    pkm = {
        'nombre':datos_pkm[0].replace('\n',''),
        'tipo':datos_pkm[1].replace('\n',''),
        'especie':datos_pkm[2].replace('\n',''),
        'hambre':datos_pkm[3].replace('\n',''),
        'felicidad':datos_pkm[4].replace('\n','')
    }

    archivo.close()

    return pkm

def initPkm (nombre:str,tipo:str,especie:str) -> dict:
    pkm = crearPkm(nombre,tipo,especie)
    savePkm(pkm)
    return pkm

def checkHambre (hambre:int) -> str:
    if (hambre in range(0,30)):
        return 'Sin hambre'

    if (hambre in range(30,80)):
        return 'Tiene Hambre'

    if (hambre >= 80):
        return 'Necesita comida'

def checkFelicidad (felicidad:int) -> str:
    if (felicidad in range(0,20)):
        return 'Triste'

    if (felicidad in range(20,50)):
        return 'Indiferente'

    if (felicidad in range(50,80)):
        return 'Contento'

    if (felicidad >= 80):
        return 'Feliz!'

def imprimirPkm (pkm:dict) -> None:
    if (pkm['tipo'] == 'misigno'):
        print(pkm['nombre'])
        print('ERROR')
    else:
        print(pkm['nombre'])
        print(pkm['especie'] + ' || ' + pkm['tipo'])
        print('Hambre => ' + pkm['hambre'] + ' => ' + checkHambre(int(pkm['hambre'])))
        print('Felicidad => ' + pkm['felicidad'] + ' => ' + checkFelicidad(int(pkm['felicidad'])))

def getPokemonInfoByID (id:int) -> dict:
    datos_pokemon = open('pokemon_list.csv')

    #lista_llaves = datos_pokemon.readline().replace('\n','').replace('"','').split(',')

    isPkm = False
    pkmInfo = {
        'tipo':'misigno',
        'especie':'desconocida',
    }
    while (True):
        pokemon = datos_pokemon.readline().replace('\n','').replace('"','').lower().split(',')
        if (pokemon[0] == str(id)):
            isPkm = True
            break

        if (pokemon == ['']):
            break

    if (isPkm):
        pkmInfo = {
            'id':str(pokemon[0]),
            'tipo':str(pokemon[3]+' / '+pokemon[4]),
            'especie':str(pokemon[1]),
        }


    datos_pokemon.close()

    return pkmInfo

def getPokemonInfoByEspecie (especie:str) -> dict:
    datos_pokemon = open('pokemon_list.csv')

    #lista_llaves = datos_pokemon.readline().replace('\n','').replace('"','').split(',')

    isPkm = False
    pkmInfo = {
        'tipo':'misigno',
        'especie':'desconocida'
    }
    while (True):
        pokemon = datos_pokemon.readline().replace('\n','').replace('"','').lower().split(',')
        if (pokemon == ['']):
            break
        
        if (pokemon[1] == str(especie).lower()):
            isPkm = True
            break

        

    if (isPkm):
        pkmInfo = {
            'id':str(pokemon[0]),
            'tipo':str(pokemon[3]+' / '+pokemon[4]),
            'especie':str(pokemon[1]),
        }


    datos_pokemon.close()

    return pkmInfo

def initPrograma () -> list[dict]:
    from os import listdir
    lista_archivos = []
    lista_pokemon = []
    for nombre_archivo in listdir('./'):
        if ('.pkm' in nombre_archivo):
            lista_archivos.append(nombre_archivo)

    for archivo in lista_archivos:
        lista_pokemon.append(loadPkm(archivo))

    return lista_pokemon

    