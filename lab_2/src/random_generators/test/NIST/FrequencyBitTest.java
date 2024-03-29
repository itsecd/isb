// Package for NIST tests for pseudorandom number generators.
package random_generators.test.NIST;

// Interface for performing tests on PRNGs.
import random_generators.test.Test;

import java.lang.Math;

/**
 * Class representing the Frequency Bit Test for PRNGs.
 */
public class FrequencyBitTest implements Test {

    /**
     * Performs the test on the specified PRNG and returns the result.
     *
     * @param bits the bits to test.
     * @return the result of the test.
     * @throws Exception if the test fails.
     */
    public double test(final int[] bits) throws Exception {
        int sum = 0;

        // Check if the input is valid.
        for (int i = 0; i < bits.length; ++i) {
            if (bits[i] == 1) {
                sum += 1;
            } else if (bits[i] == 0) {
                sum += -1;
            } else {
                throw new Exception("Input Error: Bits must be numbers 1 or 0");
            }
        }

        // Compute the erf of the test statistic.
        return Test.erfc(((double) sum / Math.sqrt(bits.length)) / Math.sqrt(2));

    }

    @Override
    public final String toString() {
        return "FrequencyBitTest";
    }
}
