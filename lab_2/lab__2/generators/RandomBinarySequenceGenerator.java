import java.util.Random;

/**
* This class generates a random binary sequence of length 128.
*/
public class RandomBinarySequenceGenerator {
/**
* The main method generates a random binary sequence and prints it to the console.
*
* @param args the command-line arguments
*/
    public static void main(String[] args) {
        Random random = new Random();

        StringBuilder binarySequence = new StringBuilder();
        for (int i = 0; i < 128; i++) {
            int randomBit = random.nextInt(2);
            binarySequence.append(randomBit);
        }

        System.out.println("The generated sequence:");
        System.out.println(binarySequence.toString());
    }
}
