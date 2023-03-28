package boj_23_0328;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class B_2075_N번째큰수 {

	private static int N;
	private static int[][] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		PriorityQueue<Integer> pq1 = new PriorityQueue<>((o1, o2) -> {
			return o2 - o1;
		});
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				pq1.add(arr[i][j]);
			}
		}
		for (int i = 1; i < N; i++)
			pq1.poll();
		System.out.println(pq1.poll());
	}

}
