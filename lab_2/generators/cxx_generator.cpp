#include <iostream>
#include <vector>
#include <random>

std::vector<int> generator(size_t size) {
    std::vector<int> rand_sequence;

    for (size_t i = 0; i < size; ++i) {
        rand_sequence.push_back(std::rand() % 2);
    }

    return rand_sequence;
}

int main() {
    std::vector<int> rand_sequence = generator(128);

    for (size_t i = 0; i < rand_sequence.size(); ++i) {
        std::cout << rand_sequence[i];
    }

    return 0;
}