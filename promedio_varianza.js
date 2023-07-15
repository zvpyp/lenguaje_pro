var {
    n: real,
    aux: real,
    prom: real,
    array1: array[100],
    i: real
}
body {

    read("ingrese tamaño del array: ", n);

    for i from 0 to n {
        read("ingresa un numero: ", aux);
        array1[i] = aux;
    };

    aux = 0;
    for i from 0 to n {
        aux = aux + array1[i];
    };

    prom = aux / n;

    aux = 0;
    for i from 0 to n {
        aux = aux + pow(array1[i] - prom, 2);
    };

    varianza = aux/n;

    write("el promedio es de ", prom);
    write("la varianza es de ", varianza);
}