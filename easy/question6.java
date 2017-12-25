package easy;

/**
 * https://projecteuler.net/problem=6
 * @author weitao92
 *
 */
public class question6 {
	
	public static void main(String args[])
	{
		int init = 5050*5050;
		for(int i = 1; i <= 100; i++)
		{
			init -= i*i;
		}
		System.out.println(init);
	}

}
