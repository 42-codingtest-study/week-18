package b5_2475;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int sum = 0;
		for (int i = 0; i < 5; i++) {
			int num = s.nextInt();
			sum += num*num;
		}
		System.out.print(sum % 10);
	}

}
