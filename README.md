# notpy
Esto no es python, es notpy.

## Ejemplo de programa
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
Los programas se componen de una sección de declaración de variables y un cuerpo:
```
var {
    declare sus variables aquí
}
body {
    cuerpo del programa
}
```
En caso de no existir variables, se puede omitir la sección de declaración:
```
body {
    cuerpo del programa
}
```

Cada sentencia dentro del body se separa por un punto y coma.

```
body {
    sentencia 1;
    sentencia 2;
    . . .
    sentencia n;
}
```


### Declaración y uso de variables
Las variables soportan el tipo `array[i]` (con *i* real, tomando la función suelo) o un real.
Las variables se declaran con la forma `id : tipo`, y se separan con coma. El array debe especificar su tamaño entre corchetes:
```
var {
    variable1 : real,
    variable2 : array[5],
    variable3 : real,
    variable4 : array[5],
    variable5 : real
}
```

En el cuerpo, a las variables se les puede asignar [expresiones aritméticas](#expresiones-aritméticas), el valor de otras variables o combinaciones de ambos. De la misma manera, se le puede asignar un valor a un índice en un arreglo.

```
body {
    variable1 = 7;
    variable2 = [1, 2, 3, 4, 5.5];
    variable3 = variable1 * 2;
    variable2[3] = 7.5;
    variable4 = variable2;
}
```

### Expresiones aritméticas
Notpy soporta suma, resta, multiplicación, divisón, potencia y raíces. La potencia y la raíz toman como primer argumento la base, y como segundo el exponente. Los valores pueden ser números reales o variables del tipo real. Las prioridades de las operaciones son las estándar de las matemáticas, y soporta el uso de paréntesis.

```
suma = variable1 + 1;
resta = 3 - 2.1;
multiplicacion = 7 * 2.1;
division = 7 / 5;
potencia = pow(7, 5);
raiz = root(8, 2);

ejemplo = (variable3 + pow(variable1, 8)) / 6;
```

### Operadores lógicos, condicionales y ciclos
Notpy soporta los operadores lógicos de igualdad (`==`), mayor que (`>`), menor que (`<`), mayor o igual que (`>=`), menor o igual que (`<=`). También posee el soporte del operador Not.
Los condicionales y ciclos son considerados sentencias, y deben finalizar con un punto y coma.

### Escritura y lectura
Se puede escribir en pantalla cadenas, variables, expresiones aritméticas y arreglos. No existe límite de argumentos. 

```
variable1 = 5;
write("hola", variable1, [2, 3, 5]);
```

```
Salida: hola 5.0 [2, 3, 5]
```

También se puede leer una entrada del usuario y guardarla en una variable

```
var {
    variable5 : real;
}
body {
    read("Escribe un número: ", variable5);
    write("Su número es: ", variable5)
}
```

```
Salida:
Escribe un número: 6
Su número es 6
```

#### Condicional if
Poseen la siguiente forma
```
if condicion {
    . . .
};
```
Por ejemplo:
```
if not variable1 > variable2 {
    variable2[2] = 7;
};
```
#### Ciclos while y for
Forma del ciclo while:
```
while condicion {
    . . .
};
```
El ciclo for no incluye el último elemento.
Forma del ciclo for:
```
for variable from inicio to final {
    . . .
};
```
Ejemplo de ciclo for:
```
for variable5 from 1 to 10 {
    write(variable5)
};
```
```
Salida:
1.0
2.0
. . .
9.0
```
El ciclo for soporta el orden inverso:
```
for variable5 from 10 to 0 {
    write(variable5)
};
```
```
Salida:
10.0
9.0
. . .
1.0
```





