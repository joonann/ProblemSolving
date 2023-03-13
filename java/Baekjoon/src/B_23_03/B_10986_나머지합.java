package B_23_03;

import java.util.Scanner;

public class B_10986_나머지합 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();

		long[] arr = new long[n + 1];

		int[] namujiArr = new int[m];
		long count = 0;

		for (int i = 1; i <= n; i++) {
			arr[i] = sc.nextLong();
		}

		for (int i = 1; i <= n; i++) {
			arr[i] += (arr[i - 1] % m);
		}

		for (int i = 1; i <= n; i++) {
			if (arr[i] % m == 0) {
				count++;
			}
			int namuji = (int) (arr[i] % m);
			namujiArr[namuji]++;
		}

		for (int i = 0; i < m; i++) {
            long a = namujiArr[i];
			if (a > 1)
				count += (a * (a - 1) / 2);
		}

		System.out.println(count);

	}
}