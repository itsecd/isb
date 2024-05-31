
/**
 * Class for generating a pseudo-random 128-bit binary sequence.
 */

public class java_generator {
     /**
     * The main entry point of the program. Generates and prints a 128-bit binary sequence.
     *
     * @param args command line arguments.
     */
    public static void main(String[] args) {
        int length = 128;
        StringBuilder binarySequence = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int randomBit = (int) (Math.random() * 2);
            binarySequence.append(randomBit);
        }

        System.out.println(binarySequence.toString());
    }
}