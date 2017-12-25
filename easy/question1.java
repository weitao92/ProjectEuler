package easy;

/**
 * https://projecteuler.net/problem=1
 * @author weitao92
 *
 */
public class question1 {
	
	public static void main(String args[])
	{
		long result = 0;
		int size1 = 1000 / 3;
		result += (((1+size1)*size1)/2) * 3;
		int size2 = 1000 / 5;
		result += (((1+size2)*size2)/2) * 5;
		result -= 1000;
		int size3 = 1000 / 15;
		result -= (1+size3)*size3/2 * 15;
		System.out.println(result);
	}

}
