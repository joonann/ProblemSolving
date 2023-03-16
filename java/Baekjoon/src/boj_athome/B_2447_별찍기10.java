package boj_athome;

import java.util.Scanner;

public class B_2447_별찍기10 {

	private static int	recursive(int n, int i, int j)
	{
		if (((i > n / 3) && (i <= n / 3 * 2)) && ((j > n / 3) && (j <= n / 3 * 2)))
			return (0);
		n /= 3;
		if (n == 1)
			return (1);
		else if (recursive(n, i % n, j % n) == 0)
			return (0);
		return (1);
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int	n = sc.nextInt();
		
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				int ret = recursive(n, i+1, j+1);
				if (ret == 0)
					sb.append(" ");
				else
					sb.append("*");
				if (j+1 == n)
					sb.append("\n");
			}
		}
		System.out.println(sb);
		
	}

}
