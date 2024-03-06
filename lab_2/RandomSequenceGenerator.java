package lab_2;

import java.util.Random;

/**
 * A class for generating a pseudo-random 128-bit binary sequence.
 */
public class RandomSequenceGenerator {

    /**
     * The main entry point of the program. Generates and prints a 128-bit binary sequence.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        // Initializing the random number generator using the current time
        Random random = new Random(System.currentTimeMillis());

        // Generating a 128-bit binary sequence
        StringBuilder sequence = new StringBuilder();
        for (int i = 0; i < 128; ++i) {
            int randomBit = random.nextInt(2);
            sequence.append(randomBit);
        }

        // Printing the generated sequence
        System.out.println(sequence.toString());
    }
}