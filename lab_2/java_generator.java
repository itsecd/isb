import java.util.Random;
import java.math.BigInteger;

public class java_generator {
    public static void main(String[] args) {
        final int sequence_length = 128;
        Random random = new Random();
        StringBuilder bit_sequence = new StringBuilder(sequence_length);

        for (int i = 0; i < sequence_length; i++) {
            int bit = random.nextInt(2);
            bit_sequence .append(bit);
        }

        System.out.println("Generated 128-bit binary sequence: " + bit_sequence .toString());
    }
}