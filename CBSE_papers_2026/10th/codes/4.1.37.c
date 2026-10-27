#include <math.h>
#include <stdio.h>

int main(void) {
    const int first_term = 4;
    const int common_difference = 4;
    int dots = 0, squares = 0;

    printf("The AP is 4, 8, 12, ...; a = %d, d = %d, a_n = 4n.\n",
           first_term, common_difference);

    while (dots < 220) {
        ++squares;
        dots += first_term + (squares - 1) * common_difference;
    }
    if (dots == 220)
        printf("With 220 dots: %d squares.\n", squares);
    else
        printf("220 dots do not complete a whole number of squares.\n");

    int n = 0;
    while (2 * n * (n + 1) < 100) ++n;
    if (2 * n * (n + 1) == 100)
        printf("With 100 dots: yes, %d squares.\n", n);
    else
        printf("With 100 dots: no whole number of squares (next total is %d dots).\n",
               2 * n * (n + 1));
    return 0;
}
