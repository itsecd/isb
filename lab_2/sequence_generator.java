package lab_2;

import java.util.Random;

public class sequence_generator {
    public static void generateRandomSequence(int length) {
        Random random = new Random();
        for (int i = 0; i < length; ++i) {
            System.out.print(random.nextInt(2));
        }
    }

    public static void main(String[] args) {
        int sequenceLength = 128;
        generateRandomSequence(sequenceLength);
    }
}