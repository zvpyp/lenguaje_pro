import csv
import analizador_lexico as al

TERMINALES = [
    "var", "{", "}", "id", ":", "," , "real", "array", "[", "]", "body", "=",
    "const_real", ";", "+", "-", "*", "/", "read", "write", "cadena", "(", ")",
    "if", "operador_relacional", "else", "while", "for", "from", "to", "not", "or", "and", "pow", "root"
    ]

class arbol_9ario:
    def __init__(self, lexema, simbolo):
        self.lexema = lexema
        self.simbolo = simbolo
        self.hijos = []
    
    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)
    
    def obtener_hijo(self, pos):
        return self.hijos[pos]
    
    def __str__(self):
        return self.simbolo + f" ({self.lexema})"
    
    def preorden(self):
        print(self)
        for hijo in self.hijos:
            hijo.preorden()
    
    def mostrar_hijos(self):
        print(f"hijos de {self}:")
        for hijo in self.hijos:
            print(hijo)

def analizador_predictivo(ruta_archivo):

    dict_tas = {}

    pila = [arbol_9ario('', '$'), arbol_9ario('', 'programa')]

    # Crea la TAS en forma de diccionario
    with open('TAS.csv', 'r') as archivo1:
        csv_tas = csv.reader(archivo1)
        lista_tas = list(csv_tas)

        for i in range(1, len(lista_tas)):
            for j in range(1, len(lista_tas[0])):
                #print(f"i: {i} j:{j}")
                # Evita los vacios
                if lista_tas[i][j] != '':
                    # diccionario de la forma (variable, terminal) = produccion
                    if lista_tas[i][j] == 'epsilon':
                        dict_tas[((lista_tas[i][0]).strip(),lista_tas[0][j].strip())] = ''
                    else:
                        dict_tas[(lista_tas[i][0].strip(),lista_tas[0][j].strip())] = lista_tas[i][j].strip()

    fuente = open(ruta_archivo).read()
    control = 0
    complex = ""
    arbol = pila[1] # la raiz del arbol es siempre "programa"

    estado = 'en proceso'

    fuente, control, complex, lexema = al.obtener_siguiente_comp_lex(fuente, control, al.tabla_simbolos)

    while estado == 'en proceso':
        #print(f"{complex}: {complex}")

        # desapilamos el tope de la pila
        tope = pila.pop()

        if tope.simbolo in TERMINALES:
            if tope.simbolo != complex:
                estado = f'error: se esperaba {tope.simbolo} y se obtuvo {complex}'
            else:
                tope.lexema = lexema

                fuente, control, complex, lexema = al.obtener_siguiente_comp_lex(fuente, control, al.tabla_simbolos)
        elif tope.simbolo == '$':
            print('fin')
            if complex == '$':
                estado = 'exito'
            else:
                estado = f'error: se esperaba fin de archivo y se obtuvo {complex}'
        else:
            if (tope.simbolo, complex) in dict_tas:
                if dict_tas[(tope.simbolo, complex)] != '':
                    elementos_apilados = dict_tas[(tope.simbolo, complex)].strip().split(' ')
                    elementos_apilados.reverse()

                    for elemento in elementos_apilados:
                        if elemento == '':
                            print(dict_tas[(tope.simbolo, complex)])
                        nodo_aux = arbol_9ario('', elemento)
                        pila.append(nodo_aux)
                        tope.agregar_hijo(nodo_aux)

                    tope.hijos.reverse()
            else:
                estado = f'error: desde {tope.simbolo} no se puede derivar una cadena que comience con {complex}'

    return arbol, estado


def arbol_a_texto(nodo_raiz, archivo, desplazamiento=''):
    archivo.write(f"{desplazamiento}{nodo_raiz}\n")

    for hijo in nodo_raiz.hijos:
        arbol_a_texto(hijo, archivo, desplazamiento+'  ')

if __name__ == '__main__':
    arbol, estado = analizador_predictivo('prueba.txt')

    arbol_texto = open('arbol_texto.txt', "w+")

    arbol_a_texto(arbol, arbol_texto)
    print(estado)