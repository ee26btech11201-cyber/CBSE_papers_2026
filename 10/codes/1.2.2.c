// code by A.Chaitanya
#include <math.h>
#include <stdio.h>

#define PI 3.14159265358979323846

static double dot(const double u[2], const double v[2])
{
    return u[0] * v[0] + u[1] * v[1];
}

static double norm(const double v[2])
{
    return sqrt(dot(v, v));
}

static void subtract(const double u[2], const double v[2], double result[2])
{
    result[0] = u[0] - v[0];
    result[1] = u[1] - v[1];
}

int main(void)
{
    const double radius = 3.0;
    const double O[2] = {0.0, 0.0};
    const double P[2] = {6.0, 0.0};
    const double contact_x = radius * radius / P[0];
    const double contact_y = sqrt(radius * radius - contact_x * contact_x);
    const double Q[2] = {contact_x, contact_y};
    const double R[2] = {contact_x, -contact_y};
    double OQ[2], OR[2], PQ[2], PR[2], QP[2], RP[2];

    subtract(Q, O, OQ);
    subtract(R, O, OR);
    subtract(Q, P, PQ);
    subtract(R, P, PR);
    subtract(P, Q, QP);
    subtract(P, R, RP);

    const double length_PQ = norm(PQ);
    const double length_PR = norm(PR);
    const double cosine = dot(PQ, PR) / (length_PQ * length_PR);
    const double angle_degrees = acos(cosine) * 180.0 / PI;
    const double tolerance = 1e-9;

    printf("Radius OQ = %.6f cm; radius OR = %.6f cm\n", norm(OQ), norm(OR));
    printf("OQ dot QP = %.10f; OR dot RP = %.10f\n", dot(OQ, QP), dot(OR, RP));
    printf("PQ = %.6f cm; PR = %.6f cm\n", length_PQ, length_PR);
    printf("Angle QPR = %.6f degrees\n", angle_degrees);

    if (fabs(norm(OQ) - radius) > tolerance ||
        fabs(norm(OR) - radius) > tolerance ||
        fabs(dot(OQ, QP)) > tolerance || fabs(dot(OR, RP)) > tolerance ||
        fabs(length_PQ - 3.0 * sqrt(3.0)) > tolerance ||
        fabs(length_PR - length_PQ) > tolerance ||
        fabs(angle_degrees - 60.0) > tolerance) {
        fprintf(stderr, "The coordinate checks failed.\n");
        return 1;
    }

    puts("All checks passed. Each tangent is 3*sqrt(3) cm; option a).");
    return 0;
}
