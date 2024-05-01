#include <iostream>
#include <random>
#include <bitset>

using namespace std;

std::bitset<128> generateRandomSequence() {
    /**
     * Generates a pseudo-random sequence of binary numbers with a length of 128 bits.
     *
     * @return A pseudo-random sequence of binary numbers with a length of 128 bits.
     */
    std::random_device rd;
    std::mt19937 gen(rd());
    std::bitset<128> random_sequence;
    for (int i = 0; i < 128; ++i) {
        random_sequence[i] = gen() & 1; 
    }

    return random_sequence;
}

int main() {
    std::bitset<128> random_sequence = generateRandomSequence();
    std::cout << "Random sequence: " << random_sequence << std::endl;
    return 0;
}