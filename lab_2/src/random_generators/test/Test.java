// Package for testing pseudorandom number generators.
package random_generators.test;

// Interface for performing tests on PRNGs.
import java.util.function.DoubleUnaryOperator;

/**
 * Interface representing a test for PRNGs.
 */
public interface Test {

    // Default value for the integration step in the integralSimpson method.
    static final double DEFAULT_INTEGRATION_FOR_INTEGRAL_STEP = 0.0001;

    // Unary operator representing the function exp(-x^2).
    static final DoubleUnaryOperator expT2 = x -> Math.exp(-Math.pow(x, 2));

    // Unary operator representing the function x^(1.5 - 1) * exp(-x).
    DoubleUnaryOperator xPow0cdot5_mul_expPowminusx = x -> Math.pow(x, 1.5 - 1) * Math.exp(-x);

    /**
     * Performs a test on the specified PRNG and returns the result.
     *
     * @param bits the bits to test.
     * @return the result of the test.
     * @throws Exception if the test fails.
     */
    public double test(final int[] bits) throws Exception;

    public String toString();

    /**
     * Computes the complementary error function (erfc) as 1 - erf(value).
     *
     * @param value the value to compute the erfc for.
     * @return the value of the erfc.
     */
    public static double erfc(double value) throws Exception{
        return 1 - erf(value);
    }

    /**
     * Computes the error function (erf) as (2 / sqrt(pi)) * integral(exp(-x^2), 0, value, DEFAULT_INTEGRATION_FOR_INTEGRAL_STEP).
     *
     * @param value the value to compute the erf for.
     * @return the value of the erf.
     */
    public static double erf(double value) throws Exception 
    {
        return ((double) 2 / Math.PI) * integralSimpson(expT2, 0, value >= 0 ? value : -value, DEFAULT_INTEGRATION_FOR_INTEGRAL_STEP);
    }

    /**
     * Computes an approximation of the definite integral of a function using the Simpson's rule.
     *
     * @param function the function to integrate.
     * @param start the lower bound of the integral.
     * @param end the upper bound of the integral.
     * @param integrationStep the step size for the integration.
     * @return the approximate value of the integral.
     * @throws Exception if the input parameters are invalid.
     */
    public static double integralSimpson(DoubleUnaryOperator function, final double start, final double end, final double integrationStep) throws Exception
    {
        if (start >= end) {
            throw new Exception("Input Error: In the integral, the value of the start is greater than the end");
        }

        if (integrationStep < 0) {
            throw new Exception("Input Error: The step in the integral is less than zero");
        }

        double numberSplits = (end - start) / integrationStep;

        double Integral = integrationStep * (function.applyAsDouble(start) + function.applyAsDouble(end)) / 6.0;

        for (int i = 1; i <= numberSplits; ++i) {
            Integral += 4.0 / 6.0 * integrationStep * function.applyAsDouble(start + integrationStep * (i - 0.5));
        }

        for (int i = 1; i <= numberSplits - 1; ++i) {
        	Integral += 2.0 / 6.0 * integrationStep * function.applyAsDouble(start + integrationStep * i);
        }

        return Integral;
    }
}
