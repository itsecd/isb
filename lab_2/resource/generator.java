// Main program to generate 128 random bits using the Java Random class.
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Random;

public class generator {

    public static void main(String[] args) {

        try (PrintWriter writer = new PrintWriter(new FileWriter("resource/random_java"))) {

            Random random = new Random();

            for (int i = 0; i < 128; ++i) {
                writer.print(Math.abs(random.nextInt()) % 2);
            }

            writer.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
