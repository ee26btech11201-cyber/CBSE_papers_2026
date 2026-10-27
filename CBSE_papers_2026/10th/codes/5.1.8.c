#include <stdio.h>

int main(void)
{
    int n;
    int numerator;
    int difference_numerator;

    printf("Enter n to find the nth term: ");
    if (scanf("%d", &n) != 1 || n < 1) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    /* a_n = -15/4 + (n - 1)(5/4) = (5n - 20)/4 */
    numerator = 5 * n - 20;
    printf("a_%d = %d/4 = %.2f\n", n, numerator, numerator / 4.0);

    /* For the question: a_16 - a_12 */
    difference_numerator = (5 * 16 - 20) - (5 * 12 - 20);
    printf("a_16 - a_12 = %d/4 = %.2f\n",
           difference_numerator, difference_numerator / 4.0);

    return 0;
}
