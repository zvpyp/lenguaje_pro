/*
    TERMINALES: {
        var, {, }, id, :, , , real, array, [, ], body, =, const_real, ;, +, -, *, /,
        read, write, cadena, (, ), if, operador_relacional, else, while, for, from, to,
        not, or, and
    }

 FORMA:
    programa ->         sec_dec_var cuerpo
    sec_dec_var ->      var { dec_vars } | epsylon
    dec_vars ->         id: tipo var_factor
    var_factor ->       , dec_vars | epsylon
    tipo ->             real | array[exp_aritmetica]
    cuerpo ->           body { sec_sentencias }
    sec_sentencias ->   sentencia; sentencia_factor
    sentencia_factor -> sec_sentencias | epsylon
    sentencia ->        asignacion | lectura | escritura | si_ent_sino |
                        ciclo_while | ciclo_for
    asignacion ->       id asig_factor
    asig_factor ->      = valor_asignado | [exp_aritmetica] = exp_aritmetica
    valor_asignado ->   exp_aritmetica | arreglo
    arreglo ->          [elementos_array]
    exp_aritmetica ->   producto arit_factor                                            // prioridad 3
    arit_factor ->      + exp_aritmetica | - exp_aritmetica | epsylon
    producto ->         numero prod_factor                                              // prioridad 2
    prod_factor ->      * producto | / producto | epsylon
    numero ->           id id_factor | const_real | (exp_aritmetica) | -numero          // prioridad 1
    id_factor ->        [exp_aritmetica] | epsylon     
    elementos_array ->  exp_aritmetica array_factor
    array_factor ->     , elementos_array | epsylon
    lectura ->          read(cadena, id)
    escritura ->        write(args_escribir)
    args_escribir ->    arg_escribir args_esc_factor
    args_esc_factor ->  , args_escribir | epsylon
    arg_escribir ->     cadena | exp_aritmetica | arreglo
    si_ent_sino ->      if condicion { sec_sentencias } sino
    sino ->             else { sec_sentencias } | epsylon
    condicion ->        conjuncion cond_or
    cond_or ->          or condicion | epsilon
    conjuncion ->       exp_relacional cond_and
    cond_and ->         and conjuncion | epsilon
    exp_relacional ->   exp_aritmetica operador_relacional exp_aritmetica | not exp_relacional | {condicion}
    ciclo_while ->      while condicion { sec_sentencias }
    ciclo_for ->        for id from exp_aritmetica to exp_aritmetica { sec_sentencias }
 */

/*

Primero(condicion) = Primero(conjuncion cond_or) = Primero(exp_relacional cond_and) = 
Primero(exp_aritmetica) = id const_real ( - not {

Primero(cond_or) = or  | { } 

Primero(cond_and → and conjuncion) = and
Primero(cond_and → epsilon) = or  | { } 

Primero(exp_relacional) = id const_real ( - not {

Especificación semántica

    estado: lista de variables utilizadas en el programa junto a sus valores actuales. La lista se inicializa
    en vacío y las variables se dan de alta con sus valores iniciales en la declaración de las variables
    Cada elemento de estado contiene nombre de la variable, tipo, tamaño (en caso de array)
    y valor correspondiente.

    programa ->         sec_dec_var cuerpo
        eval_programa(arbol, estado)
            eval_sec_dec_var(arbol.hijos[1], estado)
            eval_cuerpo(arbol.hijos[2], estado)

    sec_dec_var ->      var { dec_vars } | epsilon
        eval_sec_dec_var(arbol, estado)
            if produccion != epsilon
                eval_dec_vars(arbol.hijos[3], estado)

    dec_vars ->         id: tipo var_factor
        eval_dec_vars(arbol, estado)
            eval_tipo(arbol.hijos[3], estado, tipo, tam)

            agregar_variable(estado, arbol.hijos[1].lexema, tipo, tam)

            eval_var_factor(arbol.hijos[4], estado)

    var_factor ->       , dec_vars | epsilon
        eval_val_factor(arbol, estado)
            if produccion != epsilon
                eval_dec_vars(arbol.hijos[2], estado)

    tipo ->             real | array[exp_aritmetica]
        eval_tipo(arbol, estado, tipo, tam)
            if produccion = real
                tipo = 'real'
                tam = '0'
            else
                tipo = 'array'
                eval_exp_aritmetica(arbol.hijos[3], estado, resultado)
                tam = floor(resultado)

    cuerpo ->           body { sec_sentencias }

    sec_sentencias ->   sentencia; sentencia_factor
        eval_sec_sentencias(arbol, estado)
            eval_sentencia(arbol.hijos[1], estado)
            eval_sentencia_factor(arbol.hijos[3], estado)

    sentencia_factor -> sec_sentencias | epsylon
    sentencia ->        asignacion | lectura | escritura | si_ent_sino |
                        ciclo_while | ciclo_for
    asignacion ->       id asig_factor
        eval_asignacion(arbol, estado)
            eval_asig_factor(arbol.hijos[2], estado, arbol.hijos[1].lexema)

    asig_factor ->      = valor_asignado | [exp_aritmetica] = exp_aritmetica
        eval_asig_factor(arbol, estado, nombre_id)
            if produccion = subindice
                eval_exp_aritmetica(arbol.hijos[2], estado, resultado)
                indice = floor(resultado)
                eval_exp_aritmetica(arbol.hijos[5], estado, valor)

                asignar_valor_array_sub(estado, nombre_id, indice, valor)
            else
                eval_valor_asignado(arbol.hijos[2], estado, valor)

                asignar_valor(estado, nombre_id, valor)


    valor_asignado ->   exp_aritmetica | arreglo
    arreglo ->          [elementos_array]
    exp_aritmetica ->   producto arit_factor                                            // prioridad 3
        eval_exp_aritmetica(arbol, estado, resultado)
            eval_producto(arbol.hijos[1], estado, operando1)
            eval_arit_factor(arbol.hijos[2], estado, operando1, resultado)


    arit_factor ->      + exp_aritmetica | - exp_aritmetica | epsilon
        eval_arit_factor(arbol, estado, operando1, resultado)
            if produccion = suma
                eval_exp_aritmetica(arbol.hijos[2], estado, operando2)
                resultado = operando1 + operando2
            else if produccion = resta
                eval_exp_aritmetica(arbol.hijos[2], estado, operando2)
                resultado = operando1 - operando2
            else
                resultado = operando1

    producto ->         numero prod_factor                                              // prioridad 2
    prod_factor ->      * producto | / producto | epsylon
    numero ->           id id_factor | const_real | (exp_aritmetica) | -numero          // prioridad 1
        eval_numero(arbol, estado, resultado)
            if produccion = variable
                eval_id_factor(arbol.hijos[2], estado, arbol.hijos[1].lexema, resultado)
            else if produccion = constante_real
                resultado = convertir_a_real(arbol.hijos[1].lexema)
            else if produccion = parentesis
                eval_exp_aritmetica(arbol.hijos[2], estado, resultado)
            else
                eval_numero(arbol.hijos[2], estado, res)
                resultado = res * -1


    id_factor ->        [exp_aritmetica] | epsilon
        eval_id_factor(arbol, estado, nombre_id, resultado)
            if produccion = epsilon
                valor_real(estado, nombre_id, resultado)
            else
                eval_exp_aritmetica(arbol.hijos[2], estado, pos)
                pos = floor(pos)

                valor_arreglo_sub(estado, nombre_id, pos, resultado)
                
    
    elementos_array ->  exp_aritmetica array_factor
    array_factor ->     , elementos_array | epsylon
    lectura ->          read(cadena, id)
    escritura ->        write(args_escribir)
    args_escribir ->    arg_escribir args_esc_factor
    args_esc_factor ->  , args_escribir | epsylon
    arg_escribir ->     cadena | exp_aritmetica | arreglo
    si_ent_sino ->      if condicion { sec_sentencias } sino
    sino ->             else { sec_sentencias } | epsylon
    condicion ->        conjuncion cond_or
    cond_or ->          or condicion | epsilon
    conjuncion ->       exp_relacional cond_and
    cond_and ->         and conjuncion | epsilon
    exp_relacional ->   exp_aritmetica operador_relacional exp_aritmetica | not exp_relacional | {condicion}
        arbol.hijos[2].lexema

    ciclo_while ->      while condicion { sec_sentencias }
        eval_ciclo_while(arbol, estado)
            eval_condicion(arbol.hijos[2], estado, booleano)

            while booleano
                eval_sec_sentencias(arbol.hijos[4], estado)
                eval_condicion(arbol.hijos[2], estado, booleano)

    ciclo_for ->        for id from exp_aritmetica to exp_aritmetica { sec_sentencias }


*/

