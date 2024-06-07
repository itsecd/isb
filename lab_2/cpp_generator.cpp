#include <iostream>
#include <random>
#include <bitset>

int main() {
    const int sequence_length = 128;

    std::random_device rd;  
    std::mt19937 gen(rd()); 
    std::uniform_int_distribution<> dis(0, 1); 

    std::bitset<sequence_length> bit_sequence;

    for (int i = 0; i < sequence_length; ++i) {
        bit_sequence[i] = dis(gen);
    }

    std::cout << "Generated 128-bit binary sequence: " << bit_sequence << std::endl;

    return 0;
}