// code by A.Chaitanya
#include <math.h>
#include <stdio.h>

static double f(double x)
{
    return (x - 1.0) * (x - 1.0) - 16.0;
}

static double derivative(double x)
{
    return 2.0 * (x - 1.0);
}

static int newton_root(const char *label, double initial, double *root)
{
    const double tolerance = 1e-12;
    const int max_iterations = 50;
    double x = initial;

    printf("\nNewton-Raphson iterations from %s:\n", label);
    printf(" n              x_n                 f(x_n)\n");
    for (int n = 0; n <= max_iterations; ++n) {
        const double value = f(x);
        printf("%2d  % .12f  % .12e\n", n, x, value);
        if (fabs(value) < tolerance) {
            *root = x;
            return 0;
        }

        const double slope = derivative(x);
        if (fabs(slope) < tolerance) {
            fprintf(stderr, "Derivative is zero; Newton-Raphson cannot continue.\n");
            return 1;
        }
        x -= value / slope;
    }

    fprintf(stderr, "Newton-Raphson did not converge from %s.\n", label);
    return 1;
}

int main(void)
{
    double left_root;
    double right_root;

    if (newton_root("x_0=0", 0.0, &left_root) != 0 ||
        newton_root("x_0=6", 6.0, &right_root) != 0) {
        return 1;
    }

    printf("\nRoots: %.10f and %.10f\n", left_root, right_root);
    printf("Correct option: c) (5, -3)\n");
    return 0;
}
