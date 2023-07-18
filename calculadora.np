var {
    n1: real,
    n2: real,
    resultado: real,
    op: real
}

body {

    write("Bienvenido a la calculadora de notpy.");

    read("Si desea comenzar presione 1", op);


    if op == 1 {

        while op == 1 {

            read("Ingrese el primer número: ", n1);
            write("1. SUMA");
            write("2. RESTA");
            write("3. MULTIPLICACIÓN");
            write("4. DIVISIÓN");
            write("5. POTENCIA");
            write("6. RADICACIÓN");
            read("Seleccione su operador", op);

            read("ingrese el segundo número: ", n2);

            if op == 1 {
                resultado = n1 + n2;
            }
            else {
                if op == 2 {
                    resultado = n1 - n2;
                }
                else {
                    if op == 3 {
                        resultado = n1 * n2;
                    }
                    else {
                        if op == 4 {
                            resultado = n1 / n2;
                        } else {
                            if op == 5 {
                                resultado = pow(n1, n2);
                            }
                            else {
                                resultado = root(n1, n2);
                            };
                        };
                    };
                };
            };

            write("El resultado es: ", resultado);

            read("Si desea continuar, presione 1: ", op);
        };

    };

    write("¡Adios!");
}