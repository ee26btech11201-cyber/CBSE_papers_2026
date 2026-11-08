/* code by A.Chaitanya */
/* Find the greatest plank length that exactly measures both lengths. */
#include <stdio.h>

int main(void) {
    int a = 4 * 100 + 20; /* 4 m 20 cm = 420 cm */
    int b = 5 * 100 + 4;  /* 5 m 4 cm = 504 cm */
    int step = 0;

    while (b != 0) {
        int quotient = a / b;
        int remainder = a % b;
        printf("step %d: (a,b)=(%d,%d), q=%d, r=%d\n",
               step, a, b, quotient, remainder);
        a = b;
        b = remainder;
        ++step;
    }
    printf("HCF(420, 504) = %d cm\n", a);
    return 0;
}
