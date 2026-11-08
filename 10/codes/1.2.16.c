// code by A.Chaitanya
#include <math.h>
#include <stdio.h>

#define TOL 1e-10
#define MAX_ITER 100

static double p(double x) {
    return -x * x + 2.0 * x + 8.0;
}

static double dp(double x) {
    return -2.0 * x + 2.0;
}

static double ddp(double x) {
    (void)x;
    return -2.0;
}

static double newton_root(double x, const char *name) {
    printf("%s root iterations:\n", name);
    for (int n = 0; n < MAX_ITER; ++n) {
        double value = p(x);
        double slope = dp(x);
        printf("  n=%2d, x_n=% .10f, p(x_n)=% .3e\n", n, x, value);
        if (fabs(value) < TOL) {
            return x;
        }
        if (fabs(slope) < TOL) {
            fprintf(stderr, "Newton-Raphson stopped: p'(x_n) is too close to zero.\n");
            return NAN;
        }
        x -= value / slope;
    }
    fprintf(stderr, "Newton-Raphson did not converge for the %s root.\n", name);
    return NAN;
}

static double newton_vertex(double x) {
    puts("Vertex iterations (Newton-Raphson applied to p'(x)=0):");
    for (int n = 0; n < MAX_ITER; ++n) {
        double slope = dp(x);
        double curvature = ddp(x);
        printf("  n=%2d, x_n=% .10f, p'(x_n)=% .3e\n", n, x, slope);
        if (fabs(slope) < TOL) {
            return x;
        }
        if (fabs(curvature) < TOL) {
            fprintf(stderr, "Newton-Raphson stopped: p''(x_n) is too close to zero.\n");
            return NAN;
        }
        x -= slope / curvature;
    }
    fputs("Newton-Raphson did not converge to the vertex.\n", stderr);
    return NAN;
}

int main(void) {
    double left_root = newton_root(-1.0, "Left");
    double right_root = newton_root(5.0, "Right");
    double span = right_root - left_root;
    double vertex_x = newton_vertex(0.0);
    double vertex_y = p(vertex_x);

    if (!isfinite(left_root) || !isfinite(right_root) || !isfinite(vertex_x)) {
        return 1;
    }

    printf("\nRoots: %.10f and %.10f\n", left_root, right_root);
    printf("Span between roots: %.10f ft\n", span);
    printf("Vertex: (%.10f, %.10f)\n", vertex_x, vertex_y);
    printf("Maximum height: %.10f ft (p''(x)=%.1f < 0)\n", vertex_y, ddp(vertex_x));
    return 0;
}
