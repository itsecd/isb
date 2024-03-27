#include <iostream>
#include <ctime>

/**
 * This function initializes the random number generator using the current time and generates
 * a n-bit binary sequence, printing it to the standard output.
 * @param n number of bits in sequence
 * @return None
 */
void generate_binary_sequence(int n) {

    std::srand(static_cast<unsigned>(std::time(0)));

    for (int i = 0; i < n; ++i) {
        int random_bit = std::rand() % 2;
        std::cout << random_bit;
    }
}

/**
 * The main function calls generate_binary_sequence to generate a random binary sequence
 * and print it to the standard output.
 *
 * @return The program exit code.
 */
int main() {
    int bits;
    std::cout << "Enter number of bits for sequence: "; // for example i will use 128-bit seq
    std::cin >> bits;

    generate_binary_sequence(bits);
    return 0;
}