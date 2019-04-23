import java.io.*;
import java.util.Scanner;

/**
 * Java program responsible for processing user-input sqlite file and setting up configuration
 * file used in temoa_model system call
 */
public class FileSelector {

	// Skeleton config file used to write new, final config file with input file names
	public static final String CONFIG_TEXT = "config_sample_in";

	// Final config file called in ModelScript to run TEMOA model
	public static final String FINAL_CONFIG = "config_sample";

	// String located in CONFIG_TEXT used to indicate the user input file should be appended at end of line
	public static final String INPUT_FLAG = "--input=data";

	// TODO
	public static final String OUTPUT_FLAG = "--output=data";

	// Character encoding type used to write final config file
	public static final String CSN = "UTF-8";

	// Main method used to execute main functionality of program
    public static void main(String[] args) throws IOException, FileNotFoundException, UnsupportedEncodingException {
    
		// Establishes file that contains skeleton of text used to write to final config file
		File config_in = new File(CONFIG_TEXT);
		// Establishes Scanner used to take in user input from console, visually prompts them, and stores input
        Scanner inputReader = new Scanner(System.in);
		System.out.print("Enter name of input file: ");
		String inputFile = inputReader.nextLine();
		// TODO
        //System.out.print("Enter name of output file: ");
		//String outputFile = inputReader.nextLine();

		// Establishes Scanner used to read from skeleton config file
		Scanner fileReader = new Scanner(config_in);
		// Establishes PrintWriter used to write new, final config file
		PrintWriter out = null;
		try {
			out = new PrintWriter(FINAL_CONFIG, CSN);
		} catch(Exception e) {
			System.out.println("Error: Could not write to specified file");
        }

		// Processes skeleton config file line by line until the imput and output flags are processed, where the user input filenames are then appended 
		String line;
		while (fileReader.hasNextLine()) {
			line = fileReader.nextLine();
			if (line.contains(INPUT_FLAG)) {
				out.println("--input=data_files/" + inputFile);
			} else if (line.contains(OUTPUT_FLAG)) {
                out.println("--output=data_files/" + inputFile);
            } else {
                out.println(line);
            }
        }
		out.close();		
    }

}
