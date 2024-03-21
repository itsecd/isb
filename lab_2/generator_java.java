import java.util.Random;

class Main {
    public static void getNextRandom() {
        for (int i = 0; i < 128; i++) {
            Random random = new Random();
            int seed = random.nextInt();
            System.out.print(Math.abs(seed % 2));
        }
    }

    public static void main(String[] args) {
        getNextRandom();
    }
}
