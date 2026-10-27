#include <stdio.h>

int main(void) {
    int a = 48, b = 60, c = 65;
    int x = a, y = b;
    while (y != 0) { int r = x % y; x = y; y = r; }
    int gcd_ab = x;
    int lcm_ab = (a / gcd_ab) * b;
    x = lcm_ab; y = c;
    while (y != 0) { int r = x % y; x = y; y = r; }
    int lcm = (lcm_ab / x) * c;
    int answer = ((9999 / lcm) * lcm);
    printf("LCM(48, 60, 65) = %d\n", lcm);
    printf("Greatest multiple below 10000 = %d\n", answer);
    return 0;
}
