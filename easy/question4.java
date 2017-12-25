package easy;

import java.util.Collections;
import java.util.PriorityQueue;

/**
 * https://projecteuler.net/problem=4
 * @author weitao92
 *
 */
public class question4 {
	
	public static void main(String args[])
	{
		PriorityQueue<Integer> results = new PriorityQueue<Integer>(Collections.reverseOrder());
		for(int i = 100; i <= 999; i++)
		{
			for(int j = i; j <= 999; j++)
			{
				int temp = i*j;
				if(isPalindrome(temp))
				{
					results.add(temp);
				}
			}
		}
		
		System.out.println(results.peek());
	}
	
	private static boolean isPalindrome(int target)
	{
		String temp = Integer.toString(target);
		int size = temp.length();
		
		for(int i = 0; i < size/2; i++)
		{
			if(temp.charAt(i) != temp.charAt(size-1-i))
			{
				return false;
			}
		}
		
		return true;
	}

}
