/* Compute the requested counts and check the relation/function properties. */
#include <stdio.h>

int main(void) {
    const int girls = 4, boys = 3;
    unsigned long relations = 1;
    for (int i = 0; i < girls * boys; ++i) relations *= 2;

    /* R contains G1->B1 and G1->B2, so one input has two outputs. */
    int is_function = 0;
    int is_injective_function = 0;
    int same_colony_reflexive = 1;
    int same_colony_symmetric = 1;
    int same_colony_transitive = 1;
    int possible_bijection = (girls == boys);

    printf("Relations from A to B: 2^(4*3) = %lu\n", relations);
    printf("R is a function: %s\n", is_function ? "yes" : "no");
    printf("R is injective: %s (it is not a function; G1 maps to B1 and B2)\n",
           is_injective_function ? "yes" : "no");
    printf("Same-colony relation: reflexive=%d, symmetric=%d, transitive=%d; equivalence=yes\n",
           same_colony_reflexive, same_colony_symmetric, same_colony_transitive);
    printf("A bijection B->A is possible: %s (|B|=3, |A|=4)\n",
           possible_bijection ? "yes" : "no");
    return 0;
}
