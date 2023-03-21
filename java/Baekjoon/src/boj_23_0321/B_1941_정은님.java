package boj_23_0321;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class B_1941_정은님 {
	private static int[] dx = { 0, 1, 0 ,- 1 };
	private static int[] dy = { 1, 0, -1, 0 };
	private static char arr[][];
	private static int arr2[];
	private static ArrayList<Integer> arrX;
	private static ArrayList<Integer> arrY;
	private static int count = 0;
	private static int scount = 0;
	private static int ycount = 0;
	private static boolean[][] visited;

	public static void main(String[] args) throws Throwable {
		arr = new char[5][5];
		count = 0; // 칠공주
		scount = 0; // 다솜파
		arrX = new ArrayList<>();
		arrY = new ArrayList<>();
		Scanner sc = new Scanner(System.in);
		for (int i = 0; i < 5; i++) {
			String str = sc.next();
			for (int j = 0; j < 5; j++) {
				arr[i][j] = str.charAt(j);
			}
		}

		arr2 = new int[7];
		combination(0, 0);
		System.out.println(count);

	}

	private static void combination(int cnt, int start) {
		if (ycount > 3) {
			return;
		}
		if (cnt == 7) {
			visited = new boolean[5][5];
			if (BFS(arr2[0])) { // 인접한 경우
				if (scount >= 4) // 다솜파가 4명 이상인 경우
					count++;
			}
			return;
		}

		for (int i = start; i < 25; i++) {
			arr2[cnt] = i;
			if (arr[i / 5][i % 5] == 'S') // 다솜파일 경우 scount 1추가
				scount++;
			else
				ycount++;
			combination(cnt + 1, i + 1);
			if (arr[i / 5][i % 5] == 'S') // 다솜파일 경우 scount 1추가
				scount--;
			else
				ycount--;
			
		}
	}

	private static boolean BFS(int x) {
		Queue<int[]> q = new LinkedList<>();
		int depth = 1;
		q.offer(new int[] { x / 5, x % 5 });
		visited[x / 5][x % 5] = true;

		while (!q.isEmpty()) {
			int node[] = q.poll();
			for (int k = 0; k < 4; k++) {
				int i = node[0] + dx[k];
				int j = node[1] + dy[k];
				if (i >= 0 && j >= 0 && i < 5 && j < 5) { // 유효한 인덱스인지 확인
					// 인접한지 확인
					if (checkInArr2(i, j) && !visited[i][j]) {
						visited[i][j] = true;
						q.add(new int[] { i, j });
						depth++;
					}
				}
			}
		}
		// 인접할 경우 true
		if (depth == 7)
			return true;
		else
			return false;
	}

	private static boolean checkInArr2(int i, int j) {
		int index = 5 * i + j;
		for (int k = 0; k < 7; k++) {
			if (arr2[k] == index)
				return true;
		}
		return false;
	}

}