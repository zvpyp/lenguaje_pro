tabla_simbolos = {
    'var' : 'SECCION_VARIABLES',
    'body': 'CUERPO', 
    'for' : 'BUCLE_FOR',
    'while' : 'BUCLE_WHILE',
    'if' : 'CONDICIONAL_IF',
    'else' : 'CONDICIONAL_ELSE',
    'real' : 'TIPO_REAL',
    'array' : 'TIPO_ARRAY',
    'from' : 'FOR_DESDE',
    'to' : 'FOR_HASTA',
    'read' : 'LECTURA',
    'write' : 'ESCRITURA',
    'not':  'NOT',
    'or': 'OR',
    'and': 'AND',
}

# No sabemos si tendremos que separar en más tipos (como paréntesis, comillas)
def tipo_caracter(caracter):
    if caracter.isalpha():
        return "letra"
    elif caracter.isdigit():
        return "digito"
    elif caracter == "\"":
        return "comilla"
    elif caracter == ".":
        return "punto"
    else:
        return "otro"


def es_identificador(cadena): 
    # Agregamos solamente dos estados ya que 3 es siempre falso y a partir de 2 termina la cadena
    # no se puede agregar algo más ya que te llevaría al 3 directamente (muere en 2)
    estados = [
        {
            "letra": 1,
            "digito": 3,
            "comilla": 3,
            "punto": 3,
            "otro": 3
        },
        {
            "letra": 1,
            "digito": 1,
            "comilla": 3,
            "punto": 3,
            "otro": 2
        }
    ]

    posicion_actual = 0
    caracter_actual = ''

    estado_actual = 0
    try:
        while estado_actual not in (2,3):
            # El while recorre la cadena hasta que haya un caracter especial, o sea que esté en el 2do o 3er nodo
            # En el caso de que no esté en el 1er o 2do nodo, no recorre más ya que no sería una cadena válida
            # Primero posicionamos el lector en el primer caracter. Luego, se fija en qué posición del autómata
            # está, mediante la tabla de transiciones (es_identificador) y obtiene la salida al siguiente nodo
            # dependiendo el tipo de caracter (ver autómata de Mateo en docs)

            caracter_actual = cadena[posicion_actual]
            estado_actual = estados[estado_actual].get(tipo_caracter(caracter_actual)) 
            posicion_actual += 1
    except:
        pass

    # retorna una tupla determinando si es_identificador como primer posición, y la posición a la que lo deja como segunda
    if estado_actual == 2:
        return (True, posicion_actual - 1)
        instalarents()
    else:
        return (False, 0)


def es_cadena(cadena):
    estados = [
        {
            "letra": 5,
            "digito": 5,
            "comilla": 1,
            "otro": 5,
        },
        {
            "letra": 3,
            "digito": 3,
            "comilla": 2,
            "otro": 3,
        },
        {
            "letra": 4,
            "digito": 4,  
            "comilla": 4,
            "otro": 4,
        },
        {
            "letra": 3,
            "digito": 3,
            "comilla": 2,
            "otro": 3,
        },
    ]

    posicion_actual = 0
    caracter_actual = ''

    estado_actual = 0

    try:
        while estado_actual not in (4,5):
            caracter_actual = cadena[posicion_actual]
            estado_actual = estados[estado_actual].get(tipo_caracter(caracter_actual)) 
            posicion_actual += 1
    except:
        pass

    if estado_actual == 4:
        return (True, posicion_actual - 1)
    else:
        return (False, estado_actual)

def es_real(cadena):
    estados = [
        {
            "letra": 5,
            "digito": 1,
            "comilla": 5,
            "punto": 5,
            "otro": 5,
        },
        {
            "letra": 5,
            "digito": 1,
            "comilla": 5,
            "punto": 2,
            "otro": 4,
        },
        {
            "letra": 5,
            "digito": 3,
            "comilla": 5,
            "punto": 5,
            "otro": 5,
        },
        {
            "letra": 5,
            "digito": 3,
            "comilla": 5,
            "punto": 5,
            "otro": 4,
        }
    ]

    posicion_actual = 0
    caracter_actual = ''

    estado_actual = 0

    try:
        while estado_actual not in (4,5):
            caracter_actual = cadena[posicion_actual]
            estado_actual = estados[estado_actual].get(tipo_caracter(caracter_actual)) 
            posicion_actual += 1
    except:
        pass

    if estado_actual == 4:
        return (True, posicion_actual - 1)
    else:
        return (False, 0)

def es_simbolo_especial(cadena):
    simbolos_dobles = {
        "==": "IGUAL",
        "<=": "MENOR_IGUAL",
        ">=": "MAYOR_IGUAL",
    }

    simbolos = {
        "{" : "LLAVE_ABRE",
        "}" : "LLAVE CIERRA",
        ":" : "DOS_PUNTOS",
        "," : "COMA",
        "[" : "CORCHETE_ABRE",
        "]" : "CORCHETE_CIERRA",
        "=" : "ASIGNACION",
        ";" : "PUNTO_COMA",
        "+" : "SIGNO_MAX",
        "-" : "SIGNO_MENOS",
        "*" : "MULTIPLICACION",
        "/" : "DIVISION",
        "(" : "PARENTESIS_ABRE",
        ")" : "PARENTESIS_CIERRA",
        "<" : "MENOR",
        ">" : "MAYOR",
    }

    if cadena[0:2] in simbolos_dobles.keys():
        return(True, 2, simbolos_dobles[cadena[0:2]])
    elif cadena[0] in simbolos.keys():
        return (True, 1, simbolos[cadena[0]])
    
    return (False, 0)

def obtener_siguiente_comp_lex(fuente, control, tabla_simbolos):
    fuente = fuente[control:].lstrip()

    #print(fuente)
    #print("\n\n\n")

    nuevo_control = control
    complex = ""


    if fuente == '':
        complex = '$'
    elif es_identificador(fuente)[0]:
        nuevo_control = es_identificador(fuente)[1]
        if fuente[:nuevo_control] not in tabla_simbolos:
            tabla_simbolos.setdefault(fuente[:nuevo_control], "id")
            complex = "id"
        else:
            complex = fuente[:nuevo_control]
    elif es_real(fuente)[0]:
        nuevo_control = es_real(fuente)[1]
        complex = "const_real"
    elif es_cadena(fuente)[0]:
        nuevo_control = es_cadena(fuente)[1]
        complex = "cadena"
    elif es_simbolo_especial(fuente)[0]:
        nuevo_control = es_simbolo_especial(fuente)[1]
        complex = es_simbolo_especial(fuente)[2]
    else:
        complex = 'ERROR'

    lexema = fuente[:nuevo_control]

    return (fuente, nuevo_control, complex, lexema)


if __name__ == "__main__":
    fuente = open("aaa.txt").read()

    control = 0
    complex = ""
    while complex != '$' and complex != 'ERROR':
        fuente, control, complex, lexema = obtener_siguiente_comp_lex(fuente, control, tabla_simbolos)
        print(f"{complex}: {lexema}")
        print("\n\n\n\n")
    
    print(tabla_simbolos)