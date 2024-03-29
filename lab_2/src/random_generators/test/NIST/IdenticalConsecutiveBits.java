// Package for NIST tests for pseudorandom number generators.
package random_generators.test.NIST;

// Interface for performing tests on PRNGs.
import random_generators.test.Test;

/**
 * Class representing the Identical Consecutive Bits test for PRNGs.
 */
public class IdenticalConsecutiveBits implements Test {

    /**
     * Performs the test on the specified PRNG and returns the result.
     *
     * @param bits the bits to test.
     * @return the result of the test.
     * @throws Exception if the test fails.
     */
    public double test(final int[] bits) throws Exception {
        double sum = 0;
        double signVariables = 0;

        // Check if the input is valid.
        for (int i = 0; i < bits.length; ++i) {
            if (bits[i] == 1 || bits[i] == 0) {
                sum += bits[i];
            } else {
                throw new Exception("Input Error: Bits must be numbers 1 or 0");
            }

            if (i < bits.length - 1 && bits[i] != bits[i + 1]) {
                signVariables += 1;
            }
        }

        double unitFraction = sum / bits.length;

        // Check if the fraction of ones is close to 0.5.
        if (!(Math.abs(unitFraction - 0.5) < 2 / Math.sqrt(bits.length))) {
            return 0;
        }

        // Compute the erf of the test statistic.
        return Test.erfc((Math.abs(signVariables - 2 * unitFraction * bits.length * (1 - unitFraction))) /
                (2 * Math.sqrt(2 * bits.length) * unitFraction * (1 - unitFraction)));
    }

    @Override
    public final String toString() {
        return "IdenticalConsecutiveBits";
    }
}
