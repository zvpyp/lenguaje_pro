import automatas

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
}

def obtener_siguiente_comp_lex(fuente, control, tabla_simbolos):
    fuente = fuente[control:].lstrip()

    #print(fuente)
    #print("\n\n\n")

    nuevo_control = control
    complex = ""


    if fuente == '':
        complex = '$'
    elif automatas.es_identificador(fuente)[0]:
        nuevo_control = automatas.es_identificador(fuente)[1]
        tabla_simbolos.setdefault(fuente[:nuevo_control], "ID")
        complex = "ID"
    elif automatas.es_real(fuente)[0]:
        nuevo_control = automatas.es_real(fuente)[1]
        complex = "CONST_REAL"
    elif automatas.es_cadena(fuente)[0]:
        nuevo_control = automatas.es_cadena(fuente)[1]
        complex = "CADENA"
    elif automatas.es_simbolo_especial(fuente)[0]:
        nuevo_control = automatas.es_simbolo_especial(fuente)[1]
        complex = "SIMBOLO_ESPECIAL"
        
    
     #print(f"{complex} : {fuente[:nuevo_control]}")

    return (complex, nuevo_control, fuente)


texto = open("aaa.txt").read()

control = 0
complex = ""
while complex != '$':
    complex, control, texto = obtener_siguiente_comp_lex(texto, control, tabla_simbolos)
    print(f"{complex}: {texto[:control]}")
    print("\n\n\n\n")

print(tabla_simbolos)