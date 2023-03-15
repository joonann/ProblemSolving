package boj_23_03_14;

import java.util.Scanner;

public class B_15649_N과M {
	
	private static int N, M;
	private static int[] arr; // 원소를 저장할 배열
	private static boolean[] visited; // 중복을 제거하기 위한 방문 처리

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		N = in.nextInt();
		M = in.nextInt();
		arr = new int[M]; // 선택 숫자 저장용
		visited = new boolean[N + 1];
		permutation(0);
	}
	
	private static void permutation(int cnt) {
		if (cnt == M) {
			for (int i = 0; i < M; i++) {
				System.out.print(arr[i]+" ");
			};
			System.out.println();
			return;
		}
		for (int i = 1; i <= N; i++) {
			if (!visited[i]) {
				visited[i] = true;
				arr[cnt] = i;
				permutation(cnt + 1);
				visited[i] = false;
			}
		}
	}
}
