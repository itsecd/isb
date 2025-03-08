import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

class RandomGenerator {
    public static void main(String[] args) {
        Random rand = new Random();
        try (FileWriter writer = new FileWriter("Random_seq_java.txt")) {
            for (int i = 0; i < 128; i++) {
                int bit = rand.nextInt(2); //nextInt(2) - от 0 до 2
                writer.write(Integer.toString(bit));
            }
            System.out.println("save to Random_seq_java.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}