#include <iostream>
#include <cstdlib>
#include <ctime>

/**
 * Этот программный код генерирует случайные биты и выводит их.
 */
int main() {
    /* Устанавливаем начальное значение генератора случайных чисел на основе текущего времени */
    srand(time(nullptr));
    /* Устанавливаем длину последовательности */
    const int length = 128;
    /* Генерируем и выводим биты */
    for (int i = 0; i < length; ++i) {
        int random_bit = rand() % 2; 
        std::cout << random_bit;
    }
    std::cout << std::endl;
    return 0;
}