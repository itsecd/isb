#include <iostream>
#include <ctime>



/**
 * This function initializes the random number generator using the current time and generates
 * a size-bit binary sequence, printing it to the standard output.
 * 
 * @return None
 */
void binary_generate(int size) {

    std::srand(static_cast<unsigned>(std::time(0)));

    for (int i = 0; i < size; ++i) {
        int random_bit = std::rand() % 2;
        std::cout << random_bit;
    }
}

/**
 * The main function calls binary_generate to generate a random binary sequence
 * and print it to the standard output.
 *
 * @return The program exit code.
 */
int main() {
    int bits;
    std::cout << "Enter a number of bits" << std::endl; //128 bit
    std::cin >> bits;
    binary_generate(bits);
    return 0;
}