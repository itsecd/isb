#include <iostream>
#include <random>

void generateRandomBinarySequence() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(0, 1);

    std::cout << "The generated sequence:" << std::endl;
    for (int i = 0; i < 128; ++i) {
        int randomBit = dis(gen);
        std::cout << randomBit;
    }
}

int main(){
    generateRandomBinarySequence();
    return 0;
}