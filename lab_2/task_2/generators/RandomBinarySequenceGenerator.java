import java.util.Random;

public class RandomBinarySequenceGenerator {
    public static void main(String[] args) {
        Random random = new Random();

        // Генерация случайной последовательности бинарных данных длиной 128 бит
        StringBuilder binarySequence = new StringBuilder();
        for (int i = 0; i < 128; i++) {
            int randomBit = random.nextInt(2); // Генерация случайного бита (0 или 1)
            binarySequence.append(randomBit);
        }

        // Вывод сгенерированной последовательности
        System.out.println("The generated sequence:");
        System.out.println(binarySequence.toString());
    }
}
