import java.io.PrintWriter;
import java.io.IOException;
import java.util.Random;

public class sequence_generator {
    public static void main(String[] args) {

        Random random = new Random();

        try {
            PrintWriter pw = new PrintWriter("java_sequence.txt");
            for (int i = 0; i < 128; i++) {
                pw.print(Math.abs(random.nextInt(0, 2)));
            }
            pw.close();
        }
        catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}