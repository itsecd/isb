#include <iostream>
#include <ctime>
#include <cstdlib>

void generateRandomSequence(int length) {
    srand(time(NULL));
    for (int i = 0; i < length; ++i) {
        std::cout << rand() % 2;
    }
}

int main() {
    int sequenceLength = 128;
    generateRandomSequence(sequenceLength);
    return 0;
}