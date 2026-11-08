// code by A.Chaitanya
#include <complex.h>
#include <math.h>
#include <stdio.h>

static double complex polynomial(double complex z)
{
    return -3.0 * z * z - z - 6.0;
}

static double complex derivative(double complex z)
{
    return -6.0 * z - 1.0;
}

static int newton_root(double complex initial, double complex *root)
{
    const double tolerance = 1e-12;
    const int max_iterations = 50;
    double complex z = initial;

    printf("\nNewton-Raphson sequence from z_0 = %.0f%+.0fi:\n",
           creal(initial), cimag(initial));
    printf(" n              z_n                         |p(z_n)|\n");
    for (int n = 0; n <= max_iterations; ++n) {
        const double complex value = polynomial(z);
        printf("%2d  % .10f%+.10fi       %.3e\n",
               n, creal(z), cimag(z), cabs(value));
        if (cabs(value) < tolerance) {
            *root = z;
            return 0;
        }

        const double complex slope = derivative(z);
        if (cabs(slope) < tolerance) {
            fputs("Derivative is too close to zero.\n", stderr);
            return 1;
        }
        z -= value / slope;
    }

    fputs("Newton-Raphson did not converge.\n", stderr);
    return 1;
}

int main(void)
{
    double complex root_upper;
    double complex root_lower;
    if (newton_root(2.0 * I, &root_upper) != 0 ||
        newton_root(-2.0 * I, &root_lower) != 0) {
        return 1;
    }

    const double complex root_sum = root_upper + root_lower;
    const double complex root_product = root_upper * root_lower;
    printf("\nRoot 1: %.10f%+.10fi\n", creal(root_upper), cimag(root_upper));
    printf("Root 2: %.10f%+.10fi\n", creal(root_lower), cimag(root_lower));
    printf("Sum: %.10f%+.10fi (expected -1/3)\n",
           creal(root_sum), cimag(root_sum));
    printf("Product: %.10f%+.10fi (expected 2)\n",
           creal(root_product), cimag(root_product));

    if (cabs(root_sum + 1.0 / 3.0) > 1e-9 ||
        cabs(root_product - 2.0) > 1e-9) {
        fputs("The root sum/product checks failed.\n", stderr);
        return 1;
    }
    puts("Both checks pass. Correct option: d)");
    return 0;
}
