package easy;

/**
 * https://projecteuler.net/problem=9
 * @author weitao92
 *
 */
public class question9 {
	
	public static void main(String args[])
	{
		for(int i = 1; i < 500; i++)
		{
			for(int j = i; j < 500; j++)
			{
				if(2*i*j + 1000000 == 2000*(i+j))
				{
					System.out.println(i*j*(1000-i-j));
				}
			}
		}
	}

}
