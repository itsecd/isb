#include <iostream>
#include <cstdlib>
#include <ctime>

/*!
  \brief Pseudorandom sequence generation function
  \param number_bits The number of bits in the sequence
 */
void random_generator(int number_bits) {
    srand(time(NULL));
    for (int i = 0; i < number_bits; ++i) {
        std::cout << rand() % 2;
    }
}

int main() {
    const int NUMBER_BITS = 128;
    random_generator(NUMBER_BITS);
    return 0;
}