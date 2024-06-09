from random import randint
from lista import super_heroes, show_list, remove, search

lista_de_numeros = [1, 20, 5, 67, 3, 4, -1]
lista_de_elementos = []

for i in range(10):
    lista_de_elementos.append(chr(randint(65, 70)))



# Ejercicio 1
# print(lista_de_elementos.__len__())

# Ejercicio 2
    """
print(lista_de_elementos)

for elemento in lista_de_elementos:
        if elemento.startswith(("A", "E", "I", "O", "U")):
            lista_de_elementos.pop(lista_de_elementos.index(elemento))

for elemento in lista_de_elementos:
        if elemento.startswith(("A", "E", "I", "O", "U")):
            lista_de_elementos.pop(lista_de_elementos.index(elemento))

print(lista_de_elementos)"""

# Ejercicio 3

lista_pares=[]
lista_impares=[]
"""
for elemento in lista_de_numeros:
    if (elemento % 2) == 0:
        lista_pares.append(elemento)
    else:
        lista_impares.append(elemento)

print(lista_de_numeros)
print(lista_pares)
print(lista_impares)"""

while lista_de_numeros.__len__() != 0:
    e = lista_de_numeros.pop()
    if (e%2) == 0:
        lista_pares.append(e)
    else:
        lista_impares.append(e)

print(lista_de_numeros)
print(lista_pares)
print(lista_impares)

if remove(super_heroes, 'nombre', "Linterna Verde") != None:
    print(f"Linterna verde se removio de la lista")

indexWolverine = search(super_heroes, 'nombre', "Wolverine")
if indexWolverine != None:
    print(f"El anio de aparicion de Wolverine fue {super_heroes[indexWolverine]['año_aparicion']}")

def cantidadHeroesMarvel():
    super_marvel = 0
    super_dc = 0
    for personaje in super_heroes:
        if personaje['casa_comic'] == "Marvel Comics":
            super_marvel += 1
        else:
            super_dc += 1
    return super_marvel, super_dc

print(cantidadHeroesMarvel)

indexDoctorStrange = search(super_heroes, 'nombre', "Doctor Strange")
super_heroes[indexDoctorStrange]["casa_comic"] = "Marvel"
print(f"Casa de Doctor Strange modificada a {super_heroes[indexDoctorStrange]["casa_comic"]}")

for elemento in super_heroes:
    if elemento["biografia"].find("armadura") != -1 or elemento["biografia"].find("traje") != -1:
        print(f"El superheroe {elemento['nombre']} contiene la palabra armadura o traje en su bibliografia")
    if elemento['nombre'].startswith(('B', 'M', 'S')):
        print({elemento["nombre"]})



#Ejercicio 6
superheroes = [
    {
        "nombre": "Spider-Man",
        "anio_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Peter Parker adquirió habilidades arácnidas después de ser picado por una araña radiactiva. Ahora utiliza un traje rojo y azul para convatir el mal",
    },
    {
        "nombre": "Batman",
        "anio_aparicion": 1939,
        "casa_comic": "DC",
        "biografia": "Bruce Wayne se convierte en Batman después de presenciar el asesinato de sus padres.",
    },
    {
        "nombre": "Superman",
        "anio_aparicion": 1938,
        "casa_comic": "DC",
        "biografia": "Kal-El, un niño alienígena de Krypton, es enviado a la Tierra donde se convierte en Superman.",
    },
    {
        "nombre": "Iron Man",
        "anio_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Tony Stark, un genio multimillonario, crea una armadura de alta tecnología para luchar contra el crimen como Iron Man.",
    },
    {
        "nombre": "Linterna Verde",
        "anio_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Hal Jordan es un piloto de prueba que se convierte en el portador del anillo de poder del Cuerpo de Linternas Verdes, otorgándole increíbles habilidades y la capacidad de volar.",
    },
    {
        "nombre": "Wonder Woman",
        "anio_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Diana Prince es una princesa amazona que se convierte en la heroína conocida como Wonder Woman.",
    },
    {
        "nombre": "Hulk",
        "anio_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Bruce Banner se convierte en Hulk después de ser expuesto a radiación gamma durante un experimento.",
    },
    {
        "nombre": "Flash",
        "anio_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Barry Allen obtiene super velocidad después de ser alcanzado por un rayo y bañado en productos químicos.",
    },
    {
        "nombre": "Wolverine",
        "anio_aparicion": 1974,
        "casa_comic": "Marvel",
        "biografia": "Logan, también conocido como Wolverine, es un mutante con poderes regenerativos y garras retráctiles de adamantium.",
    },
    {
        "nombre": "Doctor Strange",
        "anio_aparicion": 1963,
        "casa_comic": "DC",
        "biografia": "Stephen Strange, un cirujano talentoso, se convierte en el Hechicero Supremo después de un accidente que lo deja sin poder usar sus manos. Aprende las artes místicas y defiende el universo contra las amenazas mágicas.",
    }
]

"""
#! criterios de orden
print(superheroes.__len__())

def by_name(item):
    return item['nombre']

peli_menor_1963 = []

for element in superheroes:
    nombre = element["nombre"]
    biografia = element["biografia"]
    casa = element["casa_comic"]
    anio = element["anio_aparicion"]

    if nombre == "Linterna Verde":
        superheroes.pop(superheroes.index(element))
    # Parte b
    if nombre == "Wolverine":
        print(f"Año de aparicion de Wolverine {anio}")
        print()
    #Parte c
    if nombre  == "Doctor Strange":
        element["casa_comic"] = "Marvel"
        print()

    if biografia.find("armadura") != -1 or biografia.find("traje") != -1:
        print(f"La biografia de {nombre} tiene la palabra armadura o traje")
        print()

    if anio < 1963:
        peli_menor_1963.append(element)
    
    if nombre == "Wonder Woman":
        print(f"La mujer maravilla pertenece a {casa}")
        print()
    
print(superheroes.__len__())
print()
print("Pelis estrenadas antes de 1963")
for element in peli_menor_1963:
    print(f"- {element["nombre"]} de la casa {element["casa_comic"]}")
    print()
    """

