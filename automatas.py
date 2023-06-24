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

if __name__ == "__main__":
    print(es_real("123.12"))
    print(es_real("123.0    pepe"))

def es_simbolo_especial(cadena):
    simbolos = {
        "{" : "LLAVE_ABRE",
        "}" : "LLAVE CIERRA",
        ":" : "DOS_PUNTOS",
        "," : "COMA",
        "[" : "CORCHETE_ABRE",
        "]" : "CORCHETE_CIERRA",
        "=" : "ASIGNACION",
        ";" : "PUNTO_COMA",
        "+" : "SUMA",
        "-" : "RESTA",
        "*" : "MULTIPLICACION",
        "/" : "DIVISION",
        "(" : "PARENTESIS_ABRE",
        ")" : "PARENTESIS_CIERRA",
    }