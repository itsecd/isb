import java.util.Random;

class Main {

    public static int[] generator(int size) {
        Random rand_generator = new Random();
        int[] rand_sequence = new int[size];

        for (int i = 0; i < size; i++) {
            rand_sequence[i] = rand_generator.nextInt(2);
        }

        return rand_sequence;
    }


    public static void main(String[] args) {
        int[] rand_sequence = generator(128);

        for (int i = 0; i < 128; i++) {
            System.out.print(rand_sequence[i]);
        }
    }
}

//01100101100111111100101110110001011100000101111101010111101100100111011000000000111100010101100101011100010111101001110011110100