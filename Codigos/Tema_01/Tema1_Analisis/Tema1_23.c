#include <stdio.h>
#define MAXDATOS 100000
#define MAXEDAD 150

int main() /* modax.c: cálculo de la moda */
{
    int i, j, n, edad, frec, maxFrec, moda, edades[MAXDATOS], frecs[MAXEDAD];
    n = 0; /* Inicializa contador de datos (talla) */
    printf("Teclear edades, finalizando con ^D\n");
    while ((n < MAXDATOS) && (scanf("%d", &edad) != EOF)) /* Lee edades */
        if ((edad >= 0) && (edad < MAXEDAD))
        {                     /* hasta EOF, */
            edades[n] = edad; /* las memoriza */
            n++;              /* y actualiza n */
        }
    //printf("Leidos %d datos; Moda=%d (frecuencia=%d)\n", n, moda, maxFrec);

    /* moda1.c: cálculo (ineficiente) de la moda */
    maxFrec = 0; /* Explora n veces edades[] para determinar cuál es la edad */
    for (i = 0; i < n; i++)
    {
        frec = 0; /* que mas se repite (moda) */
        for (j = 0; j < n; j++)
            if (edades[i] == edades[j])
                frec++;
        if (frec > maxFrec)
        {
            maxFrec = frec;
            moda = edades[i];
        }
    }
    printf("Leidos %d datos; Moda=%d (frecuencia=%d)\n", n, moda, maxFrec);

    /* moda2.c: cálculo (poco eficiente) de la moda */
    maxFrec = 0; /* Explora edades[] maxEdad veces para determinar cuál es la edad*/
    for (i = 0; i < MAXEDAD; i++)
    {             /*  */
        frec = 0; /* que m´as se repite (moda) */
        for (j = 0; j < n; j++)
            if (edades[j] == i)
                frec++;
        if (frec > maxFrec)
        {
            maxFrec = frec;
            moda = i;
        }
    }
    printf("Leidos %d datos; Moda=%d (frecuencia=%d)\n", n, moda, maxFrec);

    for (edad = 0; edad < MAXEDAD; edad++) /* máx. frecuencia (moda) */
        if (frecs[edad] > maxFrec)
        {
            maxFrec = frecs[edad];
            moda = edad;
        }
    printf("Leidos %d datos; Moda=%d (frecuencia=%d)\n", n, moda, maxFrec);

    return 0;
}
