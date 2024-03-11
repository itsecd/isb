#include <iostream>
#include <random>
#include <array>

#define SIZE 128

/**
 * A function to generate a random bit sequence of length SIZE.
 */
void generator()
{
    // Генератор случайных чисел
    std::random_device rd;
    std::mt19937 gen(rd());

    // Генерация 128 битовой псевдослучайной последовательности
    std::array<bool, SIZE> randomBits;
    for (int i = 0; i < SIZE; ++i) 
    {
        randomBits[i] = gen() % 2;
        std::cout << randomBits[i];
    }
}

/**
 * Main function to start the program.
 *
 * @return 0 on success
 */
int main() {
    generator();    
    return 0;
}
