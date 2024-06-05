import java.util.Random;

public class java_generator
{
	public static void main(String args[])
    {
        StringBuilder sequence = new StringBuilder();
        
        Random rand = new Random();
        
        for (int i = 0; i < 128; i++) {
            int rand_bit = rand.nextInt(2);
            sequence.append(rand_bit);
        }
        
        System.out.println("Random Sequence: " + sequence);
    }
}

