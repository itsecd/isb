// Package for NIST tests for pseudorandom number generators.
package random_generators.test.NIST;

// Interface for performing tests on PRNGs.
import random_generators.test.Test;

/**
 * Class representing the Longest Sequence Ones test for PRNGs.
 */
public class LongestSequenceOnes implements Test {

    // Theoretical probabilities for different block sizes.
    final static double THEORETICAL_PROBABILITY[] = {0.2148, 0.3672, 0.2305, 0.1875};

    /**
     * Performs the test on the specified PRNG and returns the result.
     *
     * @param bits the bits to test.
     * @return the result of the test.
     * @throws Exception if the test fails.
     */
    public double test(final int[] bits) throws Exception {
        return test_8_block(bits);
    }

    /**
     * Performs the test on the specified PRNG and returns the result for the 8-bit block size.
     *
     * @param bits the bits to test.
     * @return the result of the test for the 8-bit block size.
     * @throws Exception if the test fails.
     */
    public double test_8_block(final int[] bits) throws Exception {

        // Check if the input is valid.
        if (bits.length != 128) {
            throw new Exception("Input Error: The number of bits is unacceptable, exactly 128 is needed");
        }
        for (int i = 0; i < bits.length; ++i) {
            if (!(bits[i] == 1 || bits[i] == 0)) {
                throw new Exception("Input Error: Bits must be numbers 1 or 0");
            }
        }

        // Count the number of blocks with different numbers of consecutive ones.
        int blockInfo[] = new int[4];

        for (int i = 0; i < bits.length - 8; i += 8) {
            int numberConsecutiveUnits = 0;

            for (int j = 0, tmpCountUnits = 0; j < 8; ++j) {
                if (bits[j + i] == 1 && bits[i + j + 1] == 1) {
                    tmpCountUnits += 1;
                } else {
                    if (numberConsecutiveUnits <= tmpCountUnits) {
                        numberConsecutiveUnits = tmpCountUnits + 1;
                    }
                    tmpCountUnits = 0;
                }
            }

            if (numberConsecutiveUnits <= 1) {
                blockInfo[0] += 1;
            } else if (numberConsecutiveUnits == 2) {
                blockInfo[1] += 1;
            } else if (numberConsecutiveUnits == 3) {
                blockInfo[2] += 1;
            } else if (numberConsecutiveUnits >= 4) {
                blockInfo[3] += 1;
            }
        }

        // Compute the chi-square statistic.
        return Test.integralSimpson(Test.xPow0cdot5_mul_expPowminusx, 0, chiSquare(blockInfo, THEORETICAL_PROBABILITY), DEFAULT_INTEGRATION_FOR_INTEGRAL_STEP);
    }

    /**
     * Computes the chi-square statistic for the specified block sizes and theoretical probabilities.
     *
     * @param infoBlocks the block sizes.
     * @param theoreticalProbability the theoretical probabilities for each block size.
     * @return the chi-square statistic.
     * @throws Exception if the input is invalid.
     */
    public static double chiSquare(final int[] infoBlocks, final double[] theoreticalProbability) throws Exception {
        double chi_square = 0;

        if (infoBlocks.length != theoreticalProbability.length) {
            throw new Exception("Input Error: The block sizes and theoretical probabilities must be the same!");
        }

        for (int i = 0; i < infoBlocks.length; ++i) {
            chi_square += Math.pow((infoBlocks[i] - 16 * theoreticalProbability[i]), 2) / (16 * theoreticalProbability[i]);
        }

        return chi_square;
    }

    @Override
    public final String toString() {
        return "LongestSequenceOnes";
    }
}
