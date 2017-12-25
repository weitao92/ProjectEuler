package easy;

/**
 * https://projecteuler.net/problem=2
 * @author weitao92
 *
 */
public class question2 {
	
	public static void main(String args[])
	{
		int[] list = new int[50];
		list[0] = 1;
		list[1] = 2;
		long result = 2;
		for(int i = 2; i < 50; i++)
		{
			int current = list[i-2] + list[i-1];
			if(current > 4000000)
			{
				break;
			}
			
			if(current%2 == 0)
			{
				result += current;
			}
			list[i] = current;
		}
		System.out.println(result);
	}

}
