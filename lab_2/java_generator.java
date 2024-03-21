import java.util.Random;

/**
 * Класс для генерации случайных битов.
 */
public class RandomBitGenerator {
    /* Максимальный размер генерируемой последовательности битов. */
    private static final int MAXSIZE = 128;
    /* Генерирует случайные биты и выводит их на экран. */
    public void generateRandomBits() {
        Random random = new Random();
        for (int i = 0; i < MAXSIZE; i++)
            System.out.print(random.nextInt(2));
    }

    public static void main(String[] args) {
        /* Создаем объект генератора случайных битов */
        RandomBitGenerator generator = new RandomBitGenerator();
        /* Генерируем и выводим случайные биты */
        generator.generateRandomBits();
    }
}