#include <iostream>
#include <random>
#include <ctime>

#define MAX_BIT 128

using namespace std;

/**
 * A function to generate a random bit sequence of length 128.
 *
 * @return 0 on success
 */
int generator()
{
    srand(time(0));
    for (int i = 0; i < MAX_BIT; ++i)
    {
        unsigned long long rand_num = rand() % 32767;
        bool binary_num = rand_num % 2;
        cout << binary_num;
    }
    return 0;
}

/**
 * Main function to start the program.
 *
 * @return 0 on success
 */
int main()
{
    cout << generator();
}