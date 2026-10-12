#include <stdio.h>

int main() {
    float a, b, i, j, x, y;

    if (scanf("%f %f %f %f %f %f", &a, &b, &i, &j, &x, &y) != 6) {
        scanf("%f %f %f %f %f %f", &a, &b, &i, &j, &x, &y);
    }

    float hasil = ((a - b) * i / j) - (x + y);
    printf("%.3f\n", hasil);

    return 0;
}

