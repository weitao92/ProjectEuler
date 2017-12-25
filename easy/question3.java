package easy;

/**
 * https://projecteuler.net/problem=3
 * @author weitao92
 *
 */
public class question3 {
	
	public static void main(String args[])
	{
		long bb = 600851475143L;
		long init = (long)Math.sqrt((double)bb);

		for(long i = init; i >= 2; i--)
		{
			if(isPrime(i))
			{
				if(bb % i == 0)
				{
					System.out.println(i);
					System.exit(0);
				}
			}
		}	
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
