package b5_11022;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		
		int N = s.nextInt();
		
		for (int i = 1; i <= N; i++)
		{
			int a = s.nextInt();
			int b = s.nextInt();
			System.out.printf("Case #%d: %d + %d = %d\n", i, a, b, a+b);
			
		}
	}
}

