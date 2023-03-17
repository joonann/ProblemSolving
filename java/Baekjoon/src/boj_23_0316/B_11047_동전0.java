package boj_23_0316;

import java.util.Scanner;

public class B_11047_동전0 {
	private static int n, k;
	private static int[] arrCoin;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();

		arrCoin = new int[n];
		for (int i = 0; i < n; i++) {
			arrCoin[i] = sc.nextInt();
		}

		int a = n - 1;
		while (arrCoin[a] > k)
			a--;

		int ans = 0;
		while (k != 0) {
			int count = k/arrCoin[a];
			ans += count;
			k -= arrCoin[a] * count;
			a--;
		}
		System.out.println(ans);
	}
}
