// code by A.Chaitanya
#include <math.h>
#include <stdio.h>

#define SQRT3 1.73205080756887729353

static double discriminant(double k)
{
    return k * k - 24.0;
}

static int newton_root(double initial, double *root)
{
    const double tolerance = 1e-12;
    const int max_iterations = 50;
    double k = initial;

    printf("\nNewton-Raphson iterations from k_0 = %.0f:\n", initial);
    printf(" n              k_n                 D(k_n)\n");
    for (int n = 0; n <= max_iterations; ++n) {
        const double value = discriminant(k);
        printf("%2d  % .12f  % .12e\n", n, k, value);
        if (fabs(value) < tolerance) {
            *root = k;
            return 0;
        }
        if (fabs(2.0 * k) < tolerance) {
            fputs("The derivative is zero; Newton-Raphson cannot continue.\n", stderr);
            return 1;
        }
        k -= value / (2.0 * k);
    }

    fputs("Newton-Raphson did not converge.\n", stderr);
    return 1;
}

static double quadratic(double x, double k)
{
    return SQRT3 * x * x - k * x + 2.0 * SQRT3;
}

static double quadratic_derivative(double x, double k)
{
    return 2.0 * SQRT3 * x - k;
}

int main(void)
{
    double k_negative;
    double k_positive;
    if (newton_root(-4.0, &k_negative) != 0 ||
        newton_root(4.0, &k_positive) != 0) {
        return 1;
    }

    const double x_negative = k_negative / (2.0 * SQRT3);
    const double x_positive = k_positive / (2.0 * SQRT3);
    const double tolerance = 1e-9;
    printf("\nk values: %.10f and %.10f\n", k_negative, k_positive);
    printf("Repeated roots: x = %.10f and x = %.10f\n", x_negative, x_positive);
    printf("Residuals: %.3e, %.3e\n",
           quadratic(x_negative, k_negative), quadratic(x_positive, k_positive));

    if (fabs(k_negative + 2.0 * sqrt(6.0)) > tolerance ||
        fabs(k_positive - 2.0 * sqrt(6.0)) > tolerance ||
        fabs(quadratic_derivative(x_negative, k_negative)) > tolerance ||
        fabs(quadratic_derivative(x_positive, k_positive)) > tolerance) {
        fputs("The repeated-root checks failed.\n", stderr);
        return 1;
    }

    puts("Factorization: k^2 - 24 = (k - 2*sqrt(6))(k + 2*sqrt(6))");
    puts("Both values are verified; correct option: a)");
    return 0;
}
