import java.util.Scanner;

/**
 * Class for generating a pseudo-random the specified length binary sequence.
 */

public class generator {
     /**
     * The main entry point of the program. Generates and prints the specified length binary sequence.
     *
     * @param args command line arguments.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter number of bits for sequence: ");
        int length = scanner.nextInt(); // for example i will use 128-bit seq

        StringBuilder binarySequence = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int randomBit = (int) (Math.random() * 2);
            binarySequence.append(randomBit);
        }

        System.out.println(binarySequence.toString());
    }
}