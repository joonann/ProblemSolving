package boj_23_0320;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B_2178_미로탐색 {
	private static int N, M;
	private static char[][] map;
	private static boolean[][] visited;
	private static int answer;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		map = new char[N][M];
		visited = new boolean[N][M];
		answer = 0;
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String oneLine = st.nextToken();
			for (int j = 0; j < M; j++) {
				map[i][j] = oneLine.charAt(j);
			}
		}
		
		Queue<Integer> queue = new LinkedList<>();
		queue.add
		while (queue.isEmpty() == false)
		
		

	}
}
