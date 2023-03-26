package b5_11654;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int c = s.next().charAt(0); //문자 받아오는 방식때문에 틀린줄알았는데 int 형변환을 안했던 이유
		System.out.printf("%d", c);
	}
}
//String[] A = a.split(" ", 1);
//System.out.printf("%d", A[0]);	