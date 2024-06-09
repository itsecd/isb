#include <iostream>
#include <fstream>
#include <random>

using namespace std;

int main() {
    
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist(0, 1);
    
    ofstream file("../../../resources/cpp_sequence.txt");
    for (int i = 0; i < 128; i++) {
        file << dist(gen);
    }
    
    file.close();
    return 0;
}