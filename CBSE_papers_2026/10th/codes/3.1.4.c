#include <stdio.h>

int main(void) {
    const int value = 3 * 11 * 13 + 3;
    int prime = value > 1;
    for (int d = 2; d * d <= value; ++d) {
        if (value % d == 0) { prime = 0; break; }
    }
    const int divisible_by_13 = (value % 13 == 0);
    const int composite = value > 1 && !prime;
    const int odd = (value % 2 != 0);

    printf("3*11*13+3 = %d\n", value);
    printf("(A) prime: %s\n", prime ? "true" : "false");
    printf("(B) divisible by 13: %s\n", divisible_by_13 ? "true" : "false");
    printf("(C) composite: %s\n", composite ? "true" : "false");
    printf("(D) odd: %s\n", odd ? "true" : "false");
    printf("Correct option: %s\n", composite ? "(C)" : "none");
    return 0;
}
