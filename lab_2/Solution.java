// Main program to compare the output of two random number generators and save the results in JSON format.
import java.io.FileReader;
import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.reflect.TypeToken;

import random_generators.test.Test;
import random_generators.test.NIST.FrequencyBitTest;
import random_generators.test.NIST.IdenticalConsecutiveBits;
import random_generators.test.NIST.LongestSequenceOnes;

/**
 * Main class for comparing the output of two random number generators and saving the results in JSON format.
 */
public class Solution {

    /**
     * Main method.
     *
     * @param args command-line arguments.
     */
    public static void main(String[] args) {
        try {
            Gson gson = new GsonBuilder().setPrettyPrinting().create();

            String json = new String(Files.readAllBytes(Paths.get("input.json")));

            Map<String, String> dataInput = gson.fromJson(json, new TypeToken<Map<String, String>>() {}.getType());

            String filePath = Paths.get(dataInput.get("resourcePath"), dataInput.get("dataFileNameInResource")).toString();

            JsonElement jsonInput;
            jsonInput = JsonParser.parseReader(new FileReader(filePath));

            int[] javaArray = getArrayBits(jsonInput, gson, dataInput.get("nameHeaderJavaInData"));
            int[] cppArray = getArrayBits(jsonInput, gson, dataInput.get("nameHeaderCppInData"));

            List<Test> tests = generateTests();

            FileWriter writer = new FileWriter(dataInput.get("fileNameOutput"));

            String outputJsonStr = generateOutputJsonStr(gson, tests, dataInput, cppArray, javaArray);

            writer.write(outputJsonStr);
            writer.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Generates a list of tests.
     *
     * @return a list of tests.
     */
    public static List<Test> generateTests() {
        List<Test> tests = new ArrayList<>();

        tests.add(new FrequencyBitTest());
        tests.add(new IdenticalConsecutiveBits());
        tests.add(new LongestSequenceOnes());

        return tests;
    }

    /**
     * Extracts an array of bits from a JSON element.
     *
     * @param jsonInput the JSON element.
     * @param gson the Gson object.
     * @param nameHeader the name of the header in the JSON element that contains the array of bits.
     * @return an array of bits.
     */
    public static int[] getArrayBits(final JsonElement jsonInput, final Gson gson, final String nameHeader) {
        JsonArray arrayJson = jsonInput.getAsJsonObject().getAsJsonArray(nameHeader);
        List<Integer> data = gson.fromJson(arrayJson, new TypeToken<List<Integer>>() {
        }.getType());

        return data.stream().mapToInt(i -> i).toArray();
    }

    /**
     * Converts an array of integers to a string.
     *
     * @param array the array of integers.
     * @return a string representation of the array.
     */
    public static String getArrayString(int[] array) {
        return Arrays.toString(array)
                .replace("[", "")
                .replace(",", "")
                .replace(" ", "")
                .replace("]", "");
    }

    /**
     * Generates the output JSON string.
     *
     * @param gson the Gson object.
     * @param tests the list of tests.
     * @param dataInput the input data.
     * @param cppArray the array of bits from the C++ random number generator.
     * @param javaArray the array of bits from the Java random number generator.
     * @return the output JSON string.
     * @throws Exception if an error occurs while generating the JSON string.
     */
    public static String generateOutputJsonStr(final Gson gson, final List<Test> tests, final Map<String, String> dataInput, final int[] cppArray, final int[] javaArray) throws Exception {
        JsonObject cppResults = new JsonObject();
        JsonObject javaResults = new JsonObject();

        for (Test test : tests) {
            cppResults.addProperty(test.toString(), test.test(cppArray));
            javaResults.addProperty(test.toString(), test.test(javaArray));
        }

        cppResults.addProperty("Bits", getArrayString(cppArray));
        javaResults.addProperty("Bits", getArrayString(javaArray));

        JsonObject jsonOutput = new JsonObject();
        jsonOutput.add(dataInput.get("nameHeaderCppInData"), cppResults);
        jsonOutput.add(dataInput.get("nameHeaderJavaInData"), javaResults);

        return gson.toJson(jsonOutput);
    }
}