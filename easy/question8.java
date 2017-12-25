package easy;

import java.util.Scanner;

/**
 * https://projecteuler.net/problem=8
 * @author weitao92
 *
 */
public class question8 {
	
	public static void main(String args[])
	{
		Scanner in = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < 20; i++)
		{
			sb.append(in.next());
		}
		in.close();
		
		long current = 1;
		for(int i = 0; i < 13; i++)
		{
			current *= Character.getNumericValue(sb.charAt(i));
		}
		Long max = current;
		
		for(int i = 1; i <= sb.length()-13; i++)
		{
			long temp = 1;
			if(Character.getNumericValue(sb.charAt(i-1)) != 0)
			{
				temp = current / Character.getNumericValue(sb.charAt(i-1));
			}
			else
			{
				for(int j = i; j < i+12; j++)
				{
					temp *= Character.getNumericValue(sb.charAt(j));
				}
			}
			temp *= Character.getNumericValue(sb.charAt(i+12));
			current = temp;
			if(current > max)
			{
				max = current;
			}
		}
		
		System.out.println(max);
		
	}

}
