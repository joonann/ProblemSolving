package boj_23_0316;

import java.util.Scanner;

public class B_2839_설탕배달_최적화 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int minAns = Integer.MAX_VALUE;

		int a = N / 5;
		while (a >= 0) {
			int tempN = N;
			int tempAns = 0;
			tempAns += a;
			tempN -= (a * 5);
			if (tempN % 3 == 0) {
				tempAns += (tempN/3);
				if (tempAns != 0 && tempAns < minAns)
					minAns = tempAns;
			}
			a--;
		}
		if (minAns == Integer.MAX_VALUE)
			System.out.println(-1);
		else
			System.out.println(minAns);

	}

}
