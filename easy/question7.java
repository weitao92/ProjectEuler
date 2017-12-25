package easy;

/**
 * https://projecteuler.net/problem=7
 * @author weitao92
 *
 */
public class question7 {
	
	public static void main(String args[])
	{
		int index = 1;
		long current = 3;
		
		while(index < 10001)
		{
			if(current % 2 == 0)
			{
				current++;
				continue;
			}
			
			if(isPrime(current))
			{
				index++;
			}
			current++;
		}
		System.out.println(current-1);
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
