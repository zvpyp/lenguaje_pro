def tipo_caracter(caracter):
    if caracter.isalpha():
        return "letra"
    elif caracter.isdigit():
        return "digito"
    else:
        return "otro"

def es_identificador(cadena): 
    # Agregamos solamente dos estados ya que 3 es siempre falso y a partir de 2 termina la cadena
    # no se puede agregar algo más ya que te llevaría al 3 directamente (muere en 2)
    estados = [
        {
            "letra": 1,
            "digito": 1,
            "otro": 3
        },
        {
            "letra": 1,
            "digito": 1,
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
    
    if estado_actual == 2:
        return True
    else:
        return False

if __name__ == "__aaa__":
    # Cómo aceptar una cadena que no termine en caracter especial ?? Ej: "Hola" que es distinto de "Hola "
    print(es_identificador("hola"))