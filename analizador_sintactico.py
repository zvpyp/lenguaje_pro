import csv
import analizador_lexico as al

TERMINALES = [
    "var", "{", "}", "id", ":", "," , "real", "array", "[", "]", "body", "=",
    "const_real", ";", "+", "-", "*", "/", "read", "write", "cadena", "(", ")",
    "if", "operador_relacional", "else", "while", "for", "from", "to", "not", "or", "and", "$"
    ]

dict_tas = {}
# NOTA: corregir la TAS y agregar el $
pila = ['programa']

with open('TAS.csv', 'r') as archivo1:
    csv_tas = csv.reader(archivo1)
    lista_tas = list(csv_tas)

    for i in range(1, len(lista_tas)):
        for j in range(1, len(lista_tas[0])):
            #print(f"i: {i} j:{j}")
            # Evita los vacios
            if lista_tas[i][j] == '':
                continue
            # diccionario de la forma (variable, terminal) = produccion
            dict_tas[(lista_tas[i][0],lista_tas[0][j])] = lista_tas[i][j]

fuente = open("aaa.txt").read()
control = 0
complex = ""
while complex != '$' and complex != 'ERROR':
    fuente, control, complex, lexema = al.obtener_siguiente_comp_lex(fuente, control, al.tabla_simbolos)
    print(f"{complex}: {lexema}")

    # desapilamos el tope de la pila

    tope = pila.pop()

    while tope not in TERMINALES:

        # obtiene la producción separada de derecha a izquierda según la tupla
        print(f"tope: {tope}")
        print(f"lexema {lexema}")

        elementos_apilados = dict_tas[tope, lexema].split(' ')
        elementos_apilados.reverse()

        for elemento in elementos_apilados:
            pila.append(elemento)

        print(f"pila: {pila}")
        input("eee")

        tope = pila.pop()

    if tope != lexema:
        print("¡¡¡ERROR SINTÁCTICO!!!")
        break

    print(pila)
    input('aaaa \n')
        
    











