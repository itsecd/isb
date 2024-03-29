package random_generators.generators.pseudo.PRNG;

import java.time.LocalDateTime;
import java.time.LocalTime;

import random_generators.generators.Generator;

/**
 * Class representing a linear congruential generator (LCG) PRNG.
 * LCGs are relatively simple and widely used PRNGs, but they are not considered cryptographically secure.
 */
public class Linear implements Generator {

    // Default values for the LCG parameters.
    private static final int DEFALUT_SEED_FOR_GENERATOR = 25;
    private static final int DEFALUT_COEF_FOR_GENERATOR = 16807;
    private static final int DEFALUT_INCREMENT_FOR_GENERATOR = 0;
    private static final int DEFAULT_MODULUS_FOR_GENERATOR = (int) Math.pow(2, 30);

    // LCG parameters.
    protected int coef, increment, modulus, seed;

    /**
     * Constructor for the LCG PRNG.
     *
     * @param seed      the seed for the PRNG.
     * @param coef      the coefficient for the PRNG.
     * @param increment the increment for the PRNG.
     * @param modulus    the modulus for the PRNG.
     */
    public Linear(final int seed, final int coef, final int increment, final int modulus) {
        this.seed = seed;
        this.coef = coef;
        this.increment = increment;
        this.modulus = modulus;
    }

    /**
     * Default constructor for the LCG PRNG, using the default values for the parameters.
     */
    public Linear() {
        this(DEFALUT_SEED_FOR_GENERATOR);
    }

    /**
     * Constructor for the LCG PRNG, using the specified seed and the default values for the other parameters.
     *
     * @param seed the seed for the PRNG.
     */
    public Linear(final int seed) {
        this(seed, DEFALUT_COEF_FOR_GENERATOR, DEFALUT_INCREMENT_FOR_GENERATOR, DEFAULT_MODULUS_FOR_GENERATOR);
    }

    /**
     * Getter for the seed of the PRNG.
     *
     * @return the seed of the PRNG.
     */
    public final int getSeed() {
        return seed;
    }

    /**
     * Setter for the seed of the PRNG.
     *
     * @param seed the seed to set for the PRNG.
     */
    public void setSeed(final int seed) {
        this.seed = seed;
    }

    /**
     * Getter for the coefficient of the PRNG.
     *
     * @return the coefficient of the PRNG.
     */
    public final int getCoef() {
        return coef;
    }

    /**
     * Setter for the coefficient of the PRNG.
     *
     * @param coef the coefficient to set for the PRNG.
     */
    public void setCoef(final int coef) {
        this.coef = coef;
    }

    /**
     * Getter for the increment of the PRNG.
     *
     * @return the increment of the PRNG.
     */
    public final int getIncrement() {
        return increment;
    }

    /**
     * Setter for the increment of the PRNG.
     *
     * @param increment the increment to set for the PRNG.
     */
    public void setIncrement(final int increment) {
        this.increment = increment;
    }

    /**
     * Getter for the modulus of the PRNG.
     *
     * @return the modulus of the PRNG.
     */
    public final int getModulus() {
        return modulus;
    }

    /**
     * Setter for the modulus of the PRNG.
     *
     * @param modulus the modulus to set for the PRNG.
     */
    public void setModulus(final int modulus) {
        this.modulus = modulus;
    }

    /**
     * Generates a random integer.
     *
     * @return the generated integer.
     */
    @Override
    public int generate() {
        this.seed = (this.coef * this.seed + this.increment) % this.modulus;
        return this.seed;
    }

    /**
     * Generates a random integer with a maximum value.
     *
     * @param max the maximum value of the generated integer.
     * @return the generated integer.
     */
    @Override
    public int generate(final int max) {
        this.seed = (this.coef * this.seed + this.increment) % max;
        return this.seed;
    }

    /**
     * Generates a random integer for security purposes.
     *
     * @return the generated integer.
     */
    @Override
    public int randomSecurity() {
        return generate() + hashSecurity();
    }

    /**
     * Generates a random integer with a maximum value for security purposes.
     *
     * @param max the maximum value of the generated integer.
     * @return the generated integer.
     */
    @Override
    public int randomSecurity(final int max) {
        return randomSecurity() % max;
    }

    /**
     * Hashes the current time and runtime information to generate a security value.
     *
     * @return the generated security value.
     */
    private int hashSecurity() {
        return LocalTime.now().getNano() + Runtime.getRuntime().availableProcessors() + LocalDateTime.now().getMinute();
    }
}