from random import randint, choice

legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

tabla_legiones = {}
tabla_numeros = {}

def hash_legion(trooper):
    return trooper[:2]

def hash_numeros(trooper):
    return trooper[-3:]

for legion in legiones:
    tabla_legiones[legion] = []

for i in range(2000):
    trooper = f"{choice(legiones)}-{randint(1000, 9999)}"
    clave = hash_legion(trooper)
    tabla_legiones[clave].append(trooper)

for i in range(200000):
    trooper = f"{choice(legiones)}-{randint(1000, 9999)}"
    clave = hash_numeros(trooper)
    if clave not in tabla_legiones:
        tabla_numeros[clave] = []
    
    tabla_numeros[clave].append(trooper)

tabla_numeros['187'].append("FN-2187")

# troopers_187 = tabla_numeros.get('187')
# print(troopers_187)
# if "FN-2187" in troopers_187:
#     print("Encontramos al traidor")


CT_legion = tabla_legiones.get('CT')
print(CT_legion)    



