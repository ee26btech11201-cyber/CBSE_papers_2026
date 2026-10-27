#include <stdio.h>

/* S_n = 2n^2 + 13n, so a_n = S_n - S_(n-1) = 4n + 11. */
int main(void)
{
    long long n;
    printf("Enter n: ");
    if (scanf("%lld", &n) != 1 || n < 1) {
        printf("Enter a positive integer.\n");
        return 1;
    }
    printf("a_%lld = %lld\n", n, 4*n + 11);
    return 0;
}
