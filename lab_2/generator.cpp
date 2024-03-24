#include <iostream>
#include <bitset>
#include <random>

#define SIZE 128

/**
     * Generate and print binary sequence.
*/
void generate_binary_sequence(){
	std::bitset<SIZE> binary_sequence;
	std::random_device rd;
        std::mt19937 gen(rd());
	for (size_t i = 0; i < SIZE; ++i){
		binary_sequence.set(i, gen()%2);
	}
	std::cout<< binary_sequence << "\n";
}

/**
     * Main function.
     *
     * @return an iteger 0 upon exit success.
*/
int main(){
	generate_binary_sequence();
	return 0;
} 
