#include <iostream>
#include <random>

/*!
\brief Generates a random binary sequence and prints it to the console.
*/
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

/*!
\brief The main function that generates a random binary sequence.
\return The exit status of the program
*/
int main(){
    generateRandomBinarySequence();
    return 0;
}