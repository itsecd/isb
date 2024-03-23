import java.util.Random;

/**
 * The class generates a 128-bit sequence
 */
public class Generator{

    private static final int SIZE=128;

    /**
     * Entry point to the program
     * Generates a sequence of random bits
     * 
     * @param args Command Line Arguments
     */
    public static void main(String[] args) {
        Random random = new Random();

        for (int i = 0; i < 128; i++) {
            int bit = random.nextInt(2);
            System.out.print(bit);
        }
    }
}