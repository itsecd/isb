// Main program to compare the output of two random number generators (C++ and Java) and save the results as JSON.
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;

import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class GetDataJson {

    public static void main(String[] args) {

        try {
            // Define the resource path.
            String resourcePath = "resource";

            // Define the file names of the random number generators' output.
            String fileNameCpp = "random_cpp";
            String fileNameJava = "random_java";

            List<Integer> cppData = readDataFromFile(Paths.get(resourcePath, fileNameCpp).toString());
            List<Integer> javaData = readDataFromFile(Paths.get(resourcePath, fileNameJava).toString());

            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            JsonElement json = gson.toJsonTree(Map.of("cpp", cppData, "java", javaData));

            String jsonStr = gson.toJson(json);

            // Define the output file name.
            String fileNameOutput = "dataSolution.json";

            FileWriter writer = new FileWriter(Paths.get(resourcePath, fileNameOutput).toString());
            writer.write(jsonStr);
            writer.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Reads the data from a file and returns it as a list of integers.
     *
     * @param filePath the path to the file.
     * @return the data from the file as a list of integers.
     */
    private static List<Integer> readDataFromFile(String filePath) {
        List<Integer> data = new ArrayList<>();
        try {
            File file = new File(filePath);

            Scanner scanner = new Scanner(file);

            String line = scanner.nextLine();

            String[] numbers = line.split("");

            for (String number : numbers) {
                data.add(Integer.parseInt(number));
            }

            scanner.close();

            return data;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return new ArrayList<>();
        }
    }
}
