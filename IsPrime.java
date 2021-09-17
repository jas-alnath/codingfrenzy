package prime;

import java.util.*;

public class IsPrime {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter a positive integer please ");
		int userInput = scanner.nextInt();
		
		int potentialFactor = 2;
		while (userInput % potentialFactor != 0) {
			potentialFactor++;
		}
		if (potentialFactor == userInput) {
			System.out.println("the number is prime");
		}
		else {
			System.out.println("the number is not prime, factor is = " + potentialFactor);
		}
		
	}

}
