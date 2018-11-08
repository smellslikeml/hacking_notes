#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *fd;

    // Allocating memory on the heap
    char *userinput = malloc(20);
    char *outputfile = malloc(20);

    if (argc<2)
    {
        printf("Usage: %s <string to be written to /tmp/notes/>\n", argv[0]);
        exit(0);
    }

    // Copy data into heap memory
    strcpy(outputfile, "/tmp/notes");
    strcpy(userinput, argv[1]);

    // Print out some debug messages
    printf("---Debug---\n");
    printf("[*] userinput @ %p: %s\n", userinput, userinput);
    printf("[*] outputfile @ %p: %s\n", outputfile, outputfile);
    printf("[*] distance between: %d\n", outputfile - userinput);
    printf("--------------\n\n");

    // Writing the data out to the file.
    printf("Writing \"%s\" to the end of %s...\n", userinput, outputfile);
    fd = fopen(outputfile, "a");
    if (fd == NULL)
    {
        printf(stderr, "error opening %s\n", outputfile);
        exit(1);
    }
    fprintf(fd, "%s\n", userinput);
    fclose(fd);
    return 0;
}
