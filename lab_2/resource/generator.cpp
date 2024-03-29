// Main program to generate 128 random bits using the Mersenne Twister PRNG.

#include <iostream>
#include <fstream>
#include <random>

int main() {
    
    std::random_device rd;
    
    std::mt19937 gen(rd());
    
    std::uniform_int_distribution<int> dist(0, 255);

    std::vector<int> numbers;
    
    for (int i = 0; i < 128; i++) {
        numbers.push_back(dist(gen) % 2);
    }

    std::ofstream file("random_cpp");
    
    for (int number : numbers) {
        file << number;
    }
    
    file.close();

    return 0;
}
