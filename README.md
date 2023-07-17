# notpy
Esto no es python.

## Ejemplo de programa
Los programas se componen de una sección de declaración de variables (innecesaria en caso de no haber variables) y un cuerpo.

```
var {
    variable1: real,
    variable2: real,
    variable3: array[5],
    variable4: real,
    id: real
}
body {
    variable1 = 7.9;
    variable2 = 11.1;

    read("escribime algo y lo guardo", variable4);
    write(variable4);
    write("mensaje", variable1, 5 + 6.1, [2.2, 5.1]);

    if variable1 == variable2 {
        write("holaa");
    }
    else {
        write("adios");
    };

    while variable2 > variable3[1] {
        variable3[1] = variable2 + 1;
    };

    for id from 0 to 10 {
        write(id, ": bien!");
    };
}
```

## Índice
### Forma de los programas
### Declaración y uso de variables
### Expresiones aritméticas
### Operadores lógicos, condicionales y ciclos
### Escritura y lectura
