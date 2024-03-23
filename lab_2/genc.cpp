#include <iostream>
#include <ctime>

#define SIZE 128

/**
 * @brief Generates a sequence of random bits
 * 
 * 
 * The function allows you to generate a sequence of random bits 
 * of length size
 */
void generator()
{
    std::srand(std::time(NULL));
    for (size_t i = 0; i < SIZE; ++i)
    {
        size_t bit = rand() % 2;
        std::cout << bit;
    }
}

/**
 * @brief The entry point to the program
 * 
 * The function calls the generator() function to generate a 
 * random sequence
 * 
 * @return 0 if the program completed successfully
 */
int main()
{
    std::cout << "Generator C++/" << std::endl;
    generator();
    return 0;
}