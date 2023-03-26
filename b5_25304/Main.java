package b5_25304;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int X = s.nextInt();
		int N = s.nextInt();
		int sum = 0;
		for (int i = 0; i < N; i++) {
			int a = s.nextInt();
			int b = s.nextInt();
			sum += a * b;
		}
		if (sum == X)
			System.out.printf("Yes");
		else
			System.out.printf("No");
	}

}
