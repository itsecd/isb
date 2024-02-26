import java.util.Random;

public class RandomGeneratorJava {
    /**
    * Pseudorandom sequence generation function
    * @param number_bits The number of bits in the sequence
    */
    public static void random_generator(int number_bits) {
        Random random = new Random();
        for (int i = 0; i < number_bits; i++) {
            System.out.print(random.nextInt(2));
        }
        System.out.println();
    }

    public static void main(String[] args) {
        final int NUMBER_BITS = 128;
        random_generator(NUMBER_BITS);
    }
}