import analizador_sintactico as sintactico
import math as m

def agregar_variable(estado, nombre_id, tipo, tam):
    if tipo == 'real':
        estado[nombre_id] = 0
    else:
        estado[nombre_id] = [0] * m.floor(abs(tam))

def asignar_valor(estado, nombre_id, valor, indice):
    if indice == -1:
        # caso real
        estado[nombre_id] = valor
    else:
        # array
        # hay que verificar que en esa posición exista el array
        estado[nombre_id][indice] = valor

def obtener_valor(estado, nombre_id, pos=-1):
    if pos == -1:
        # caso real
        valor = float(estado[nombre_id])
    else:
        # caso array
        # verificar que exista
        valor = float(estado[nombre_id][pos])
    return valor

def eval_programa(arbol, estado):
    eval_sec_dec_var(arbol.hijos[0], estado)
    eval_cuerpo(arbol.hijos[1], estado)

def eval_sec_dec_var(arbol, estado):
    if arbol.hijos:
        eval_dec_vars(arbol.hijos[2], estado)

def eval_dec_vars(arbol, estado):
    tipo, tam = eval_tipo(arbol.hijos[2], estado)

    agregar_variable(estado, arbol.hijos[0].lexema, tipo, tam)

    eval_var_factor(arbol.hijos[3], estado)

def eval_var_factor(arbol, estado):
    if arbol.hijos:
        eval_dec_vars(arbol.hijos[1], estado)

def eval_tipo(arbol, estado):
    tipo = ''
    tam = 0
    if arbol.hijos[0].lexema == 'real':
        tipo = 'real'
    else:
        tipo = 'array'
        tam = m.floor(eval_exp_aritmetica(arbol.hijos[2], estado))
    return tipo, tam

def eval_cuerpo(arbol, estado):
    eval_sec_sentencias(arbol.hijos[2], estado)

def eval_sec_sentencias(arbol, estado):
    eval_sentencia(arbol.hijos[0], estado)
    eval_sentencia_factor(arbol.hijos[2], estado)

def eval_sentencia_factor(arbol, estado):
    if arbol.hijos:
        eval_sec_sentencias(arbol.hijos[0], estado)

def eval_sentencia(arbol, estado):
    hijo = arbol.hijos[0]

    if hijo.simbolo == 'asignacion':
        eval_asignacion(hijo, estado)
    elif hijo.simbolo == 'lectura':
        eval_lectura(hijo, estado)
    elif hijo.simbolo == 'escritura':
        eval_escritura(hijo, estado)
    elif hijo.simbolo == 'si_ent_sino':
        eval_si_ent_sino(hijo, estado)
    elif hijo.simbolo == 'ciclo_while':
        eval_ciclo_while(hijo, estado)
    else:
        eval_ciclo_for(hijo, estado)

def eval_asignacion(arbol, estado):
    eval_asig_factor(arbol.hijos[1], estado, arbol.hijos[0].lexema)

def eval_asig_factor(arbol, estado, nombre_id):
    indice = -1
    if arbol.hijos[0].lexema == '[':
        indice = m.floor(eval_exp_aritmetica(arbol.hijos[1], estado))
        valor = eval_exp_aritmetica(arbol.hijos[4], estado)
    else:
        valor = eval_valor_asignado(arbol.hijos[1], estado)

    asignar_valor(estado, nombre_id, valor, indice)

def eval_valor_asignado(arbol, estado):
    hijo = arbol.hijos[0]

    if hijo.simbolo == 'exp_aritmetica':
        valor_asignado = eval_exp_aritmetica(hijo, estado)
    else:
        valor_asignado = eval_arreglo(hijo, estado)
    return valor_asignado

# aaaaaaaaaaaa
def eval_arreglo(arbol, estado):
    array = []
    eval_elementos_array(arbol.hijos[1], estado, array)
    return array

def eval_exp_aritmetica(arbol, estado):
    operando1 = eval_producto(arbol.hijos[0], estado)
    resultado = eval_arit_factor(arbol.hijos[1], estado, operando1)
    return resultado

def eval_arit_factor(arbol, estado, operando1):

    if arbol.hijos:
        primer_hijo = arbol.hijos[0]

        if primer_hijo.lexema == '+':
            operando2 = eval_exp_aritmetica(arbol.hijos[1], estado)
            resultado = operando1 + operando2
        elif primer_hijo.lexema == '-':
            operando2 = eval_exp_aritmetica(arbol.hijos[1], estado)
            resultado = operando1 - operando2
    else:
        resultado = operando1
    
    return resultado

def eval_producto(arbol, estado):
    operando1 = eval_numero(arbol.hijos[0], estado)
    resultado = eval_prod_factor(arbol.hijos[1], estado, operando1)
    return resultado

def eval_prod_factor(arbol, estado, operando1):
    """
    print('en prod_factor')
    for hijo in arbol.hijos:
        print(hijo)
    input('awa')
    """

    if arbol.hijos:
        primer_hijo = arbol.hijos[0]
        if primer_hijo.simbolo == '*':
            operando2 = eval_exp_aritmetica(arbol.hijos[1], estado)
            resultado = operando1 * operando2
        elif primer_hijo.simbolo == '/':
            operando2 = eval_exp_aritmetica(arbol.hijos[1], estado)
            resultado = operando1 / operando2
    else:
        resultado = operando1
    return resultado


def eval_numero(arbol, estado):
    for hijo in arbol.hijos:
        print(hijo)
    input('algo')


    hijo = arbol.hijos[0]

    if hijo.simbolo == 'id':
        resultado = eval_id_factor(arbol.hijos[1], estado, hijo.lexema)
    elif hijo.simbolo == 'const_real':
        resultado = float(hijo.lexema)
    elif hijo.simbolo == '(':
        resultado = eval_exp_aritmetica(arbol.hijos[1], estado)
    elif hijo.simbolo == '-':
        resultado = -(eval_exp_aritmetica(arbol.hijos[1], estado))
    elif hijo.simbolo == 'pow':
        base = eval_exp_aritmetica(arbol.hijos[2], estado)
        exponente = eval_exp_aritmetica(arbol.hijos[4], estado)
        resultado = base ** exponente
    else:
        #root
        base = eval_exp_aritmetica(arbol.hijos[2], estado)
        exponente = eval_exp_aritmetica(arbol.hijos[4], estado)
        resultado = base ** (1/exponente)
    
    return resultado

def eval_id_factor(arbol, estado, nombre_id):
    if arbol.hijos:
        pos = m.floor(eval_exp_aritmetica(arbol.hijos[1], estado))
        resultado = obtener_valor(estado, nombre_id, pos)
    else:
        resultado = obtener_valor(estado, nombre_id)
    return resultado

def eval_elementos_array(arbol, estado, array):
    array.append(eval_exp_aritmetica(arbol.hijos[0]))
    eval_array_factor(arbol.hijos[1], estado, array)

def eval_array_factor(arbol, estado, array):
    if arbol.hijos:
        eval_elementos_array(arbol, estado, array)

def eval_lectura(arbol, estado):
   cadena = arbol.hijos[2].lexema
   nombre_id = arbol.hijos[4].lexema
   valor = input(cadena)
   asignar_valor(estado, nombre_id, valor, -1)

def eval_escritura(arbol, estado):
    eval_args_escribir(arbol.hijos[2], estado)
    print('')

def eval_args_escribir(arbol, estado):
    eval_arg_escribir(arbol.hijos[0], estado)
    eval_args_esc_factor(arbol.hijos[1], estado)

def eval_args_esc_factor(arbol, estado):
    if arbol.hijos:
        eval_args_escribir(arbol.hijos[1], estado)

def eval_arg_escribir(arbol, estado):
    hijo = arbol.hijos[0]

    if hijo.simbolo == 'cadena':
        print(hijo.lexema, end=' ')
    elif hijo.simbolo == 'exp_aritmetica':
        print(eval_exp_aritmetica(arbol.hijos[0],estado), end=' ')
    else:
        print(eval_arreglo(arbol.hijos[0], estado), end=' ')

def eval_si_ent_sino(arbol, estado):
    if eval_condicion(arbol.hijos[1], estado):
        eval_sec_sentencias(arbol.hijos[3], estado)
    else:
        eval_sino(arbol.hijos[5], estado)

def eval_sino(arbol, estado):
    if arbol.hijos:
        eval_sec_sentencias(arbol.hijos[2], estado)

def eval_condicion(arbol, estado):
    operador1 = eval_conjuncion(arbol.hijos[0], estado)
    resultado = eval_cond_or(arbol.hijos[1], estado, operador1)
    return resultado

def eval_cond_or(arbol, estado, operador1):
    if arbol.hijos:
        operador2 = eval_condicion(arbol.hijos[1], estado)
        resultado = operador1 or operador2
    else:
        resultado = operador1
    return resultado

def eval_conjuncion(arbol, estado):
    operador1 = eval_exp_relacional(arbol.hijos[0], estado)
    resultado = eval_cond_and(arbol.hijos[1], estado, operador1)
    return resultado

def eval_cond_and(arbol, estado, operador1):
    if arbol.hijos:
        operador2 = eval_condicion(arbol.hijos[1], estado)
        resultado = operador1 and operador2
    else:
        resultado = operador1
    return resultado

def eval_exp_relacional(arbol, estado):
    hijo = arbol.hijos[0]

    if hijo.lexema == '{':
        resultado = eval_condicion(arbol.hijos[1], estado)
    elif hijo.lexema == 'not':
        resultado = not(eval_exp_relacional(arbol.hijos[1], estado))
    else:
        exp1 = eval_exp_aritmetica(arbol.hijos[0], estado)
        exp2 = eval_exp_aritmetica(arbol.hijos[2], estado)
        op = arbol.hijos[1].lexema

        if op == '>':
            resultado = exp1 > exp2
        elif op == '<':
            resultado = exp1 < exp2
        elif op == '>=':
            resultado = exp1 >= exp2
        elif op == '<=':
            resultado = exp1 <= exp2
        else:
            resultado = exp1 == exp2
    
    return resultado

def eval_ciclo_while(arbol, estado):
    while (eval_condicion(arbol.hijos[1], estado)):
        eval_sec_sentencias(arbol.hijos[3], estado)

def eval_ciclo_for(arbol, estado):
    inicio = m.floor(eval_exp_aritmetica(arbol.hijos[3], estado))
    fin = m.floor(eval_exp_aritmetica(arbol.hijos[5], estado))
    step = 1

    if inicio > fin:
        step = -1
    
    for _ in range(inicio, fin, step):
        eval_sec_sentencias(arbol.hijos[7], estado)




estado_semantico = {}

arbol, estado = sintactico.analizador_predictivo('prueba.js')

arbol_texto = open('arbol_texto.txt', '+w')

sintactico.arbol_a_texto(arbol, arbol_texto)

eval_programa(arbol, estado_semantico)

print(estado)