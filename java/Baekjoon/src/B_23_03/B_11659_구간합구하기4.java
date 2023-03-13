package B_23_03;

import java.util.Scanner;

public class B_11659_구간합구하기4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int dp[] = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			dp[i] = dp[i - 1] + sc.nextInt();
		}
		
		int[] start = new int[M];
		int[] end = new int[M];
		
		for (int i = 0; i < M; i++) {
			start[i] = sc.nextInt();
			end[i] = sc.nextInt();
		}
		
		for (int i = 0; i < M; i++) {
			System.out.println(dp[end[i]] - dp[start[i] - 1]);			
		}
	}
}
