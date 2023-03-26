package b5_10952;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		
		int N = 0;
		int a;
		int b;
		do {
			a = s.nextInt();
			b = s.nextInt();
			if (a == 0 && b == 0) break;
			System.out.println(a+b);
			
		} while(a != 0 && b != 0);
	}

}
