import csv
import analizador_lexico as al

TERMINALES = [
    "var", "{", "}", "id", ":", "," , "real", "array", "[", "]", "body", "=",
    "const_real", ";", "+", "-", "*", "/", "read", "write", "cadena", "(", ")",
    "if", "operador_relacional", "else", "while", "for", "from", "to", "not", "or", "and", "$"
    ]

# NOTA: corregir la TAS y agregar el $

class arbol_9ario:
    def __init__(self, lexema):
        self.lexema = lexema
        self.hijos = []
    
    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)
    
    def obtener_hijo(self, pos):
        return self.hijos[pos]
    
    def __str__(self):
        return self.lexema
    
    def inorden(self):
        print(self)
        for hijo in self.hijos:
            hijo.inorden()
        input(f'acá terminan los hijos de {self}')


dict_tas = {}

pila = [arbol_9ario('$'), arbol_9ario('programa')]

# Crea la TAS en forma de diccionario
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


fuente = open("prueba.txt").read()
control = 0
complex = ""
arbol = pila[1] # la raiz del arbol es siempre "programa"

while complex != '$' and complex != 'ERROR':
    fuente, control, complex, lexema = al.obtener_siguiente_comp_lex(fuente, control, al.tabla_simbolos)
    #print(f"{complex}: {complex}")

    # desapilamos el tope de la pila

    tope = pila.pop()

    while tope.lexema not in TERMINALES:

        
        # obtiene la producción separada de derecha a izquierda según la tupla
        #print(f"tope: {tope.lexema}")
        #print(f"complex: {complex}")

        if tope.lexema != "epsilon" and tope.lexema != "":
            

            elementos_apilados = dict_tas[tope.lexema, complex].split(' ')
            elementos_apilados.reverse()

            for elemento in elementos_apilados:
                nodo_aux = arbol_9ario(elemento)
                pila.append(nodo_aux)
                tope.agregar_hijo(nodo_aux)

            tope.hijos.reverse()

            #for pos, nodo in enumerate(pila):
            #    print(f'elemento {pos}: {nodo}')

            tope = pila.pop()
        else:
            tope = pila.pop()

    
    if tope.lexema != complex:
        print(f"tope: {tope.lexema}")
        print(f"complex: {complex}")
        print("¡¡¡ERROR SINTÁCTICO!!!")
        break