import java.util.Random;

public class Main {

   /**
   * This method generates binary sequence.
   * @return string of binary values.
   */
    public static String generateBinarySequence() {
        final int SIZE = 128;
        Random random = new Random();
        StringBuilder binarySequence = new StringBuilder();
        for (int i = 0; i < SIZE; i++) {
            binarySequence.append(random.nextInt(2)); 
        }

        return binarySequence.toString();
    }

   /**
   * This is the main method which makes use of generateBinarySequence method.
   * @param args Unused.
   * @return Nothing.
   */
    public static void main(String[] args) {
        System.out.println(generateBinarySequence());
    }
}
