var {
    n: real,
    aux: real,
    distancia: real,
    array1: array[100],
    array2: array[100],
    i: real
}
body {

    read("ingrese tamaño de los arrays: ", n);

    for i from 0 to n {
        read("ingresa un numero para el primer array: ", aux);
        array1[i] = aux;
    };

    aux = 0;

    for i from 0 to n {
        read("ingresa un numero para el segundo array: ", aux);
        array2[i] = aux;
    };

    aux = 0;

    for i from 0 to n {
        aux = aux + pow((array1[i] - array2[i]), 2);
    };

    distancia = root(aux, 2);

    write("la distancia es de: ", distancia);
}