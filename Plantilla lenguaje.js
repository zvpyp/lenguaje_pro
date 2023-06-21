/*
    Este es un modelo de referencia que vamos a utilizar para la construcción
*/

// NOTA: el ; va inclusive despues de if, while y for, considerados sentencias.

// Sección de declaración variables (dec_var)
var {
    variable1: real,
    variable2: real,
    variable3: array[5] //array de 5 elementos (0 a 4)
}


// Cuerpo del programa
body {
    //asignación
    variable1 = 7.9;
    variable2 = 11.1 + (2.2 - 3.4 * 2) / 6;
    variable3 = [1.1, 2.2, 3.3, 4.4, 5.5];

    read("mensaje"); // lectura

    //escritura, no estoy seguro si se refiere a arreglos como literales
    write("mensaje", variable1, 5 + 6.1, [2.2, 5.1]);

    // si_ent_sino (puede no contener el sino)
    if variable1 == variable2 {
        //CUERPO DE IF
    }
    else {
        //CUERPO ELSE
    };

    while variable2 > variable3 {
        // Cuerpo while
    };

    for i from 0 to 10 {
        // cuerpo for
    };
}

/*
    TERMINALES: {
        var, {, }, id, :, , , real, array, [, ], body, =, const_real, ;, +, -, *, /,
        read, write, cadena, (, ), if, operador_relacional, else, while, for, from, to
    }

 FORMA:
    programa ->         sec_dec_var cuerpo
    sec_dec_var ->      var { dec_vars }
    dec_vars ->         id: tipo, dec_vars | id: tipo | epsylon
    tipo ->             real, array[exp_aritmetica]
    cuerpo ->           body { sec_sentencias }
    sec_sentencias ->   sentencia; sec_sentencias | sentencia;
    sentencia ->        asignacion | lectura | escritura | si_ent_sino |
                        ciclo_while | ciclo_for
    asignacion ->       id = valor_asignado | id[exp_aritmetica] = valor_asignado
    valor_asignado ->   exp_aritmetica | arreglo
    arreglo ->          [elementos_array]
    exp_aritmetica ->   exp_aritmetica + producto | exp_aritmetica - producto | producto// prioridad 3
    producto ->         producto * numero | producto / numero | numero                  // prioridad 2
    numero ->           id | const_real |(exp_aritmetica)                               // prioridad 1
    elementos_array     exp_aritmetica | exp_aritmetica, elementos_array
    lectura ->          read(cadena)
    escritura ->        write(args_escribir)
    args_escribir ->    arg_escribir, args_escribir | arg_escribir
    arg_escribir ->     cadena | exp_aritmetica | arreglo
    si_ent_sino ->      if condicion { sec_sentencias } sino
    sino ->             else { sec_sentencias } | epsilon
    condicion ->        valor_a_comparar operador_relacional valor_a_comparar
    valor_a_comparar -> exp_aritmetica
    ciclo_while ->      while condicion { sec_sentencias }
    ciclo_for ->        for id from exp_aritmetica to exp_aritmetica { sec_sentencias }
 */
