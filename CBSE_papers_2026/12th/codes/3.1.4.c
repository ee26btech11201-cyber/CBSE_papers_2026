#include <stdio.h>

/* Check all answer choices using matrix multiplication dimensions. */
int main(void) {
    const int lhs_rows = 3, lhs_cols = 1;
    const int result_rows = 3, result_cols = 3;
    const int options[4][2] = {{3, 1}, {1, 3}, {1, 1}, {3, 3}};
    const char labels[4] = {'A', 'B', 'C', 'D'};

    for (int i = 0; i < 4; ++i) {
        int a_rows = options[i][0];
        int a_cols = options[i][1];
        int product_is_defined = (lhs_cols == a_rows);
        int product_has_required_order =
            product_is_defined && lhs_rows == result_rows && a_cols == result_cols;

        printf("Option (%c): A is %d x %d: %s\n", labels[i], a_rows, a_cols,
               product_has_required_order ? "valid" : "invalid");
        if (product_has_required_order) {
            printf("Therefore, the order of A is %d x %d.\n", a_rows, a_cols);
        }
    }
    return 0;
}
