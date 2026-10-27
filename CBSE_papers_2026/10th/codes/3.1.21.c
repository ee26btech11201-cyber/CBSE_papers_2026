/* Find the greatest plank length that exactly measures both lengths. */
#include <stdio.h>

int main(void) {
    int a = 4 * 100 + 20; /* 4 m 20 cm = 420 cm */
    int b = 5 * 100 + 4;  /* 5 m 4 cm = 504 cm */
    int x = a, y = b;
    while (y != 0) {
        int rem = x % y;
        x = y;
        y = rem;
    }
    printf("HCF(%d, %d) = %d cm\n", a, b, x);
    return 0;
}
