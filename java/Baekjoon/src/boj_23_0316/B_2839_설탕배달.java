package boj_23_0316;

import java.util.Scanner;

public class B_2839_설탕배달 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int ans = 0;
		int count = 0;

		if (N % 10 == 7 && N >= 17) {
			while (N != 17) {
				N -= 10;
				ans += 2;
			}
			ans += 5;
			N = 0;
		} else if (N % 10 == 1 && N >= 11) {
			while (N != 11) {
				N -= 10;
				ans += 2;
			}
			ans += 3;
			N = 0;
		} else if (N % 10 == 2 && N >= 12) {
			while (N != 12) {
				N -= 10;
				ans += 2;
			}
			ans += 4;
			N = 0;
		} else if (N % 10 == 4 && N >= 14) {
			while (N != 14) {
				N -= 10;
				ans += 2;
			}
			ans += 4;
			N = 0;
		} else if (N % 10 == 8) {
			while (N > 8) {
				N -= 10;
				ans += 2;
			}
			ans += 2;
			N = 0;
		} else {
			while (N > 10) {
				N -= 10;
				ans += 2;
			}
			if (N % 3 == 0) {
				count = N / 3;
				N -= count * 3;
				ans += count;
			} else if (N % 5 == 0) {
				count = N / 5;
				N -= count * 5;
				ans += count;
			}
		}

		if (N == 0)
			System.out.println(ans);
		else
			System.out.println(-1);
	}

}
