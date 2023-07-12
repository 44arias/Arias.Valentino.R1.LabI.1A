import random
import re
import os

def formatear_csv(path):
    lista_nueva = []
    lista_x = []
    with open(path, encoding="utf8") as archivo:
        for linea in archivo:
            linea = linea.replace("\n", "")
            lista_x = linea.split(",")
            lista_nueva.append(lista_x)

        lista_nueva.pop(0)

    return lista_nueva

# formatear_csv_lol = formatear_csv("movies.csv")

def lista_a_diccionario(path, lista, key, key_2, key_3, key_4):
    lista = list(
        map(
            lambda pelicula: {
                key: pelicula[0],
                key_2: pelicula[1],
                key_3: pelicula[2],
                key_4: random.randint(100, 240),
            },
            formatear_csv(path),
        )
    )
    print("Se guardó la lista a diccionario")

    return lista

# lista_lol = lista_a_diccionario("movies.csv", formatear_csv_lol, "id_peli", "titulo", "genero", "duracion")

def imprimir_lista(lista):
    for pelicula in lista:
        print(f"ID: {pelicula['id_peli']}")
        print(f"TITULO: {pelicula['titulo']}")
        print(f"GENERO: {pelicula['genero']}")
        print(f"DURACION: {pelicula['duracion']}")
        print("--------------------------------------------------------------------------")

# imprimir_lista(lista_lol)

def guardar_tiempos(lista, path):
    path_copia = path + "_copia.csv"

    with open(path, "r", encoding="utf8") as archivo_origen:
        with open(path_copia, "w", encoding="utf8") as archivo_copia:
            for linea in archivo_origen:
                archivo_copia.write(linea)
    
    with open(path, "w", encoding="utf8") as archivo:
        for pelicula in lista:
            linea = f"{pelicula['id_peli']},{pelicula['titulo']},{pelicula['genero']},{pelicula['duracion']}\n"
            archivo.write(linea)

    print(f"Se creó el archivo de películas con los tiempos actualizados: {path}")

def filtrar_por_tipo(path, lista, key):
    while True:
        genero = input("Ingrese el género a buscar: ").capitalize()
        peliculas_finded = []

        for pelicula in lista:
            if re.search(genero, pelicula[key]):
                peliculas_finded.append(pelicula)

        if not peliculas_finded or genero == "":
            os.system("cls")
            print(f"No se encontraron películas con el género '{genero}'")
            break

        with open(path, "w", encoding="utf8") as archivo:
            for pelicula in peliculas_finded:
                pelicula_total = f"{pelicula['id_peli']},{pelicula['titulo']},{pelicula['genero']},{pelicula['duracion']}"
                pelicula_total = pelicula_total.replace("'", "").replace("(", "").replace(")", "")
                archivo.write(pelicula_total + "\n")

        print(f"Se creó el archivo de películas con el género '{genero}'")

        break

def mostrar_duraciones_en_orden(lista: list, key: str, key_2: str):
    # lista.sort(key=lambda x: (x[key], x[key_2]))

    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][key] > lista[j][key]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            if lista[i][key] == lista[j][key]:
                if lista[i][key_2] < lista[j][key_2]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    print("Peliculas ordenadas alfabeticamenmte y por duración")

    imprimir_lista(lista)

    return lista

def guardar_peliculas(path: str, lista: list):
    archivo = open(path, "w", encoding="utf8")

    for pelicula in lista:
        archivo.write(f"{pelicula['id_peli']},{pelicula['titulo']},{pelicula['genero']},{pelicula['duracion']}\n")

    archivo.close()

    print("Se creó el archivo de películas")