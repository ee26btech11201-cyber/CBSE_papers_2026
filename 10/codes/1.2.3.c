// code by A.Chaitanya
#include <stdio.h>

static int is_prime(int value)
{
    if (value < 2) {
        return 0;
    }
    for (int divisor = 2; divisor * divisor <= value; ++divisor) {
        if (value % divisor == 0) {
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    const int value = 3 * 11 * 13 + 3;
    const int option_a_prime = is_prime(value);
    const int option_b_divisible_by_13 = value % 13 == 0;
    const int option_c_composite = value > 1 && !option_a_prime;
    const int option_d_odd = value % 2 != 0;

    printf("Expression value: %d\n", value);
    printf("(a) prime: %s\n", option_a_prime ? "true" : "false");
    printf("(b) divisible by 13: %s (remainder %d)\n",
           option_b_divisible_by_13 ? "true" : "false", value % 13);
    printf("(c) composite: %s\n", option_c_composite ? "true" : "false");
    printf("(d) odd: %s\n", option_d_odd ? "true" : "false");

    if (!option_a_prime && !option_b_divisible_by_13 &&
        option_c_composite && !option_d_odd) {
        puts("Correct option: c)");
        return 0;
    }

    fputs("The options did not produce the expected result.\n", stderr);
    return 1;
}
