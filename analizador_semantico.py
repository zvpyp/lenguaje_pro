import analizador_semantico as semantico
import math as m


def eval_programa(arbol, estado):
    eval_sec_dec_var(arbol.hijos[0], estado)
    eval_cuerpo(arbol.hijos[1], estado)

def eval_sec_dec_var(arbol, estado):
    if not arbol.hijos:
        eval_dec_vars(arbol.hijos[2], estado)

def eval_dec_vars(arbol, estado):
    tipo, tam = eval_tipo(arbol.hijos[2], estado, tipo, tam)

    agregar_variable(estado, arbol.hijos[0].lexema, tipo, tam)

    eval_var_factor(arbol.hijos[3], estado)

def eval_var_factor(arbol, estado):
    if not arbol.hijos:
        eval_dec_vars(arbol.hijos[1], estado)

def eval_tipo(arbol, estado):
    tipo = ''
    tam = 0
    if arbol.hijos[0].lexema == 'real':
        tipo = 'real'
    else:
        tipo = 'array'
        tam = math.floor()







estado_semantico = {}

arbol, estado = semantico.analizador_predictivo('prueba.txt')

arbol_texto = open('arbol_texto.txt', "w+")

arbol_a_texto(arbol, arbol_texto)
print(estado)