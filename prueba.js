var {
    variable1: real,
    variable2: real,
    variable3: array[5],
    variable4: real,
    id: real
}
body {
    variable1 = 7.9;
    variable2 = 11.1 + (2.2 * 3.4 - 2) / 6;
    variable3 = [1.1, 2.2, 3.3, 4.4, 5.5];

    read("mensaje", variable4);
    write("mensaje", variable1, 5 + 6.1, [2.2, 5.1]);

    if variable1 == variable2 {
        write("holaa");
    }
    else {
        write("nashee");
    };

    while variable2 > variable3 {
        write("sos ", 3*5, " veces alto capo");
    };

    for id from 0 to 10 {
        write(id, ": nashe");
    };
}