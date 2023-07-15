var {
    n: real,
    aux: real,
    distancia: real,
    array1: array[100],
    array2: array[100],
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
}