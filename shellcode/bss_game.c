#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

int game(int);
int jackpot();

int main(int argc, char *argv[])
{
    static char buffer[20];
    static int (*function_ptr) (int user_pick);

    if (argc < 2)
    {
        printf("Usage: %s <a number 1 - 20> \n", argv[0]);
        printf("Use %s help or %s -h for more help. \n", argv[0], argv[0]);
        exit(0);
    }

    // Seed the randomizer
    srand(time(NULL));

    // Set the function pointer to point to the game function.
    function_ptr = game;

    // Print out some debug messages
    printf("---DEBUG---\n");
    printf("[before strcpy] function_ptr @ %p\n", &function_ptr, function_ptr);
    strcpy(buffer, argv[1]);

    printf("[*] buffer @ %p: %s\n", buffer, buffer);
    printf("[after strcpy] function_ptr @ %p: %p\n", &function_ptr, function_ptr);

    if (argc<2)
    {
        printf("[*] argv[2] @ %p\n", argv[2]);
        printf("------------\n\n");
    }

    // If the first argument is "help" or "-h" display a help message
    if ((!strcmp(buffer, "help")) || (!strcmp(buffer, "-h")))
    {
        printf("Help Text:\n\n");
        printf("This is a game of change.\n");
        printf("It costs 10 credits to play, which will be\n");
        printf("automatically deducted from your account.\n\n");
        printf("To play, simply guess a number 1 through 20\n");
        printf("  %s <guess>\n", argv[0]);
        printf("If you guess the number I am thinking of,\n");
        printf("you will win the jackpot of 100 credits!\n");
    }
    else
    // Otherwise, call the game function using the function pointer
    {
        function_ptr(atoi(buffer));
    }
}
    int game(int user_pick)
{
    int rand_pick;

    // Make sure the user picks a number from 1 to 20
    if ((user_pick < 1) || (user_pick > 20))
    {
        printf("You must pick a number from 1 - 20\n");
        printf("Use help or -h for help\n");
        return 0;
    }
    
    printf("Playing the game of chance..\n");
    printf("10 credits have been subtracted from your account\n");
    /* <insert code to subtract 10 credits from an account> */

    // Pick a random number from 1 to 20
    rand_pick = (rand()%20) + 1;

    printf("You picked: %d\n", user_pick);
    printf("Random Value: %d\n", rand_pick);

    // If the random number matches the user's number, call jackpot()
    if (user_pick == rand_pick)
    {
        jackpot();
    } else
    {
        printf("Sorry, you didn't win this time..\n");
    }
}
    
    // Jackpot function, give the user 100 credits.
    int jackpot()
    {
        printf("You just won the jackpot!\n");
        printf("100 credits have been added to your account.\n");
    }
