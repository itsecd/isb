package generators;
import java.util.Random;

/**
 * This class generates a random binary sequence of length 128.
 */
public class generator_j {
/**
 * This method generates a random bit   
 */
    public static int random_generator(){
        Random random = new Random();
        return random.nextInt(2);   
    }
/**
 * This method generates a sequence of random numbers and outputs them
 * @param num_bits - the number of bits in the sequence
 */
    public static void random_sequece(int num_bits){
        for(int i = 0; i < num_bits; i++){
            System.out.print(random_generator());
        }
        System.out.println();
    }
/**
* The main method generates a random binary sequence and prints it to the console.
* @param args the command-line arguments
*/
public static void main(String[] args) {
        final int NUMBER_BITS = 128;
        random_sequece(NUMBER_BITS);
    }
}