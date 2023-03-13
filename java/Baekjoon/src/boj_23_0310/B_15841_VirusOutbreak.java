package boj_23_0310;

import java.util.Scanner;

public class B_15841_VirusOutbreak {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] arr = new int[491];
		arr[0] = 0;
		arr[1] = 1;
		for (int i = 2; i < 491; i++) {
			arr[i] = arr[i - 1] + arr[i - 2];
		}

		while (true) {
			int a = sc.nextInt();
			if (a == -1)
				break;
			else	
				System.out.println("Hour " + a + ": " + arr[a] + " cow(s) affected");
		}
		sc.close();
	}
	// 왜 안 되는지 도저히 모르겠네... writer 로 한번에 출력해야하는듯..
}
