package lab_2.generates_binary;

import java.util.Random;

public class generate_java {

    public static boolean[] generateRandomSequence() {
        Random random = new Random();
        boolean[] randomSequence = new boolean[128];

        for (int i = 0; i < 128; i++) {
            randomSequence[i] = random.nextBoolean();
        }

        return randomSequence;
    }

    public static void main(String[] args) {
        boolean[] randomSequence = generateRandomSequence();
        StringBuilder sequenceString = new StringBuilder();

        
        for (boolean bit : randomSequence) {
            sequenceString.append(bit ? "1" : "0");
        }

        System.out.println("Random sequence: " + sequenceString);
    }
}
