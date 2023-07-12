import os
from b_funciones import *

def menu_opciones():
    os.system("cls")
    print("""
1- Cargar datos del archivo
2- Imprimir datos de las películas
3- Asignar tiempos
4- Crear archivo películas por género
5- Ordenar películas
6- Guardar películas en nuevo archivo de texto
7- Salir""")

    while True:
        try:
            opcion = int(input("Ingrese la opción: "))
            while opcion < 1 or opcion > 7:
                opcion = int(input("ERROR, ingrese un número que esté dentro de las opciones: "))

            return opcion

        except ValueError:
            print("ERROR, eso no es un número")
            os.system("pause")
            os.system("cls")

lista_dic_transformadex = []
lista_ordenada = []
flag_lista_csv = False
flag_peliculas_ordenadas = False
path_csv = input("Ingrese la ruta del archivo CSV: ")
path_csv_copia = "movies_genero.csv"
path_txt = "movies_ordenadas.txt"

def elegir_opcion(opcion, lista_dic_transformadex, lista_ordenada):
    salir = None

    if opcion == 1:
        os.system("cls")
        lista_csv= formatear_csv(path_csv)
        lista_dic_transformadex = lista_a_diccionario(path_csv, lista_csv, "id_peli", "titulo", "genero", "duracion")
    elif opcion == 2:
        os.system("cls")
        imprimir_lista(lista_dic_transformadex)
    elif opcion == 3:
        os.system("cls")
        guardar_tiempos(lista_dic_transformadex, path_csv)
    elif opcion == 4:
        os.system("cls")
        filtrar_por_tipo(path_csv_copia, lista_dic_transformadex, "genero")
    elif opcion == 5:
        os.system("cls")
        lista_ordenada = mostrar_duraciones_en_orden(lista_dic_transformadex, "genero", "duracion")
    elif opcion == 6:
        os.system("cls")
        guardar_peliculas(path_txt, lista_ordenada)
    elif opcion == 7:
        os.system("cls")
        salir = input("Seguro que desea salir? s/n: ")
        pass

    return salir, lista_dic_transformadex, lista_ordenada

while True:
    opcion = menu_opciones()

    try:
        open(path_csv, encoding='utf-8')

    except FileNotFoundError:
        print("ERROR, el archivo csv no existe")
        break

    if opcion == 7 or (opcion == 1 and not flag_lista_csv):
        flag_lista_csv = True

    if opcion == 5 and not flag_peliculas_ordenadas:
        flag_peliculas_ordenadas = True

    elif not flag_peliculas_ordenadas and opcion == 6:
        os.system("cls")
        print("Las peliculas no estan ordenadas, primero hay que ordenarlas")
        os.system("pause")
        continue

    elif not flag_lista_csv:
        os.system("cls")
        print("ERROR, La lista no está creada. Por favor, cree la lista antes de continuar")
        os.system("pause")
        continue

    opcion_salir, lista_dic_transformadex, lista_ordenada = elegir_opcion(opcion, lista_dic_transformadex, lista_ordenada)

    if opcion_salir == 's':
        os.system("cls")
        break
    os.system("pause")
