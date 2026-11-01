/* code by A.Chaitanya */
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#include "libs/randfun.h"

int main(int argc, char **argv)
{
    char *end;
    long count;
    unsigned long seed;

    if (argc != 4) {
        fprintf(stderr, "Usage: %s output-file count seed\n", argv[0]);
        return EXIT_FAILURE;
    }

    count = strtol(argv[2], &end, 10);
    if (*end != '\0' || count <= 0 || count > INT_MAX) {
        fputs("count must be a positive integer\n", stderr);
        return EXIT_FAILURE;
    }

    seed = strtoul(argv[3], &end, 10);
    if (*end != '\0') {
        fputs("seed must be an integer\n", stderr);
        return EXIT_FAILURE;
    }

    srand((unsigned int)seed);
    uniform(argv[1], (int)count);
    return EXIT_SUCCESS;
}
