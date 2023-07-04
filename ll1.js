/*
    TERMINALES: {
        var, {, }, id, :, , , real, array, [, ], body, =, const_real, ;, +, -, *, /,
        read, write, cadena, (, ), if, operador_relacional, else, while, for, from, to
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