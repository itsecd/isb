/**

@file generator_c.cpp
@brief Program for generating a random sequence of bits of a specified length. */
#include <iostream>
#include <random>

/**

@brief Generates a random number 0 or 1.

@return Random number 0 or 1.
*/
int random_generator(){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(0, 1);

    return dis(gen);
}
/**

@brief Generates a random sequence of bits of a specified length.
@param num_bits The length of the sequence in bits. */ 
void random_sequence(const size_t& num_bits){
    for(size_t i = 0; i < num_bits; i++){ 
        std::cout << random_generator(); 
    }
    std::cout << std::endl; 
}
/**

@brief Entry point of the program. Generates a random sequence of bits of length 128 bits.
@return Successful program termination. */ 
int main() { 
    const size_t NUMBER_BITS = 128; 
    random_sequence(NUMBER_BITS); 
    return 0; 
}