package easy;

/**
 * https://projecteuler.net/problem=10
 * @author weitao92
 *
 */
public class question10 {
	
	public static void main(String args[])
	{
		long result = 0;
		for(long i = 2; i < 2000000; i++)
		{
			if(isPrime(i))
			{
				result += i;
			}
		}
		
		System.out.println(result);
	}
	
	private static boolean isPrime(long target)
	{
		for(long i = 2; i*i <= target; i++)
		{
			if(target % i == 0)
			{
				return false;
			}
		}
		
		return true;
	}

}
