package boj_23_0317;

import java.util.Arrays;
import java.util.Scanner;

public class B_1920_수찾기 {

	private static int N, M;
	private static int[] arrN;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		arrN = new int[N];
		for (int i = 0; i < N; i++) {
			arrN[i] = sc.nextInt();
		}
		
		Arrays.sort(arrN);
		
		M = sc.nextInt();
		for (int i = 0; i < M; i++) {
			int number = sc.nextInt();
			if (checkInN(number) == 1)
				System.out.println(1);
			else
				System.out.println(0);
		}

	}
	
	private static int checkInN(int a) {
		
		int start = 0;
		int end = N-1;
		while (start <= end) {
			int mid = (start + end) / 2;
			if (a < arrN[mid]) {
				end = mid-1;
			}
			else if (a > arrN[mid]) {
				start = mid+1;
			}
			else
				return 1;
		}
		return 0;
	}

}
