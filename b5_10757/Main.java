package b5_10757;
import java.util.Scanner;
import java.math.BigInteger;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		
		BigInteger A = s.nextBigInteger();
		BigInteger B = s.nextBigInteger();
		BigInteger sum = A.add(B);
		System.out.print(sum);
	}

}
