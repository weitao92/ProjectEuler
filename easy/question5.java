package easy;

/**
 * https://projecteuler.net/problem=5
 * @author weitao92
 *
 */
public class question5 {
	
	public static void main(String args[])
	{
		long current = 1;
		for(long i = 2; i <= 20; i++)
		{
			long gcd = GCD(current, i);
			current = (current*i) / gcd;
		}
		System.out.println(current);
	}
	
	private static long GCD(long a, long b)
	{
		while(b != 0)
		{
			long temp = b;
			b = a%b;
			a = temp;
		}
		
		return a;
	}

}
