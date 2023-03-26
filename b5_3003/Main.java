package b5_3003;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int[] chess = {1, 1, 2, 2, 2, 8};
		int[] input = new int[6];
		int[] output = new int[6];
		for(int i = 0; i < 6; i++) {
			input[i] = s.nextInt();
			output[i] = chess[i] - input[i];
			System.out.printf(output[i]+" ");
		}
	}

}
