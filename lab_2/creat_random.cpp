#include <iostream>
#include <cstdlib> 
using namespace std;

int main() {
    int arr[128];
    for (int i = 0; i < 128; ++i) {
        arr[i] = rand() % 2;
    }

    for (int i = 0; i < 128; ++i) {
        cout << arr[i];
    }

    return 0;
}
//11001000001111111010100100100110101011101101101110100111111001000000000101000110110000001001011000111110001010110001111000101110