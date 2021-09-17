package summation;

public class SumOfNumbers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sum = 0;
		int number = 1;
		while (number <= 100) {
			sum = sum + number;
			number = number + 1;
		}
        System.out.println("sum of numbers from 1 to 100 " + sum);
	}

}
