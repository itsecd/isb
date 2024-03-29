package random_generators.generators;

/**
 * Interface for random number generators.
 *
 * Random number generators are used to generate sequences of numbers that appear to be random.
 * They are used in a variety of applications, such as simulations, games, and cryptography.
 *
 * This interface defines the basic methods that all random number generators must implement.
 * These methods are:
 *
 * * `generate()`: Generates a random integer.
 * * `generate(final int max)`: Generates a random integer with a maximum value.
 * * `randomSecurity()`: Generates a random integer for security purposes.
 * * `randomSecurity(final int max)`: Generates a random integer with a maximum value for security purposes.
 */
public interface Generator {

    /**
     * Generates a random integer.
     *
     * @return the generated integer.
     */
    public int generate();

    /**
     * Generates a random integer with a maximum value.
     *
     * @param max the maximum value of the generated integer.
     * @return the generated integer.
     */
    public int generate(final int max);

    /**
     * Generates a random integer for security purposes.
     *
     * @return the generated integer.
     */
    public int randomSecurity();

    /**
     * Generates a random integer with a maximum value for security purposes.
     *
     * @param max the maximum value of the generated integer.
     * @return the generated integer.
     */
    public int randomSecurity(final int max);
}