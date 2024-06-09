
tabla_de_cadenas = {}
tabla_de_caracteres = {}

def codificar_tabla_ASCII(tabla_de_caracteres):
    for num in range(0, 256):
        caracter = chr(num)
        codificado = codificar(caracter)
        valor = encriptar(codificado)
        if valor not in tabla_de_caracteres:
            tabla_de_caracteres[valor] = []
        tabla_de_caracteres[valor].insert(0, caracter)

def codificar(character):
    caracteres = []
    character = ord(character)
    character_ascii = character * 37
    comp = complemento(character)
    digitos = dividir_entero_en_digitos(character_ascii)
    transformar_digito_a_caracter(digitos, comp, caracteres)
    caracteres.append(chr(comp))
    return ''.join(caracteres)
            
def complemento(character):
    if character <= 78:
        return 79 + character - 32
    elif character > 78:
        return 32 + character - 79

def dividir_entero_en_digitos(num):
    str1 = str(num)
    A = 1
    result = []
    for i in range(0, len(str1), A):
        # convert to int, after the slicing process
        result.append(int(str1[i : i + A]))
    return result

def transformar_digito_a_caracter(digitos, comp, caracteres):
    for digito in digitos:
        digito = (digito * digito) + comp 
        digito = chr(digito)
        caracteres.append(digito)

# def bernstein(string):
#     h = 0
#     for caracter in string:
#         h = h * 33 + ord(caracter)
#     return h%256

import hashlib
"""Con esta libreria podes asignar una cadena a un valor unico numerico"""
def encriptar(mensaje):
    hash_obj = hashlib.sha256(mensaje.encode())
    return hash_obj.hexdigest()

# def crear_tabla(mensaje_codificado):

#     bloques_codificados = [mensaje_codificado[i:i+5] for i in range(0, len(mensaje_codificado), 5)]
#     for bloque_codificado in bloques_codificados:
#         clave = bloque_codificado
#         valor = bernstein(clave)
#         if valor not in tabla_de_cadenas:
#             tabla_de_cadenas[valor] = []
#             tabla_de_cadenas[valor].append(clave)

def desencriptar(mensaje_codificado):
    texto_desencriptado = ""
    bloques_codificados = [mensaje_codificado[i:i+5] for i in range(0, len(mensaje_codificado), 5)]
    for bloque_codificado in bloques_codificados:
        clave = bloque_codificado
        valor = encriptar(clave)
        letra = tabla_de_caracteres.get(valor)
        if letra:
            letra = letra[0]
            texto_desencriptado += letra
    return texto_desencriptado

"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

codificar_tabla_ASCII(tabla_de_caracteres)
"""Leer y decodificar mensajes"""
file_path = "mensaje_3.txt"
with open(file_path, "r") as file:
    mensaje_codificado = file.read()
    texto = desencriptar(mensaje_codificado)

print(texto)


# print(tabla_de_caracteres)