package boj_23_0321;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_1976_여행계획짜기 {

	private static int[] parent;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken()); // 도시의 수 (<=200)
		st = new StringTokenizer(br.readLine());
		int M = Integer.parseInt(st.nextToken()); // 여행 계획에 속한 도시의 수 (<=1000)

		parent = new int[N+1];
		for (int i = 1; i <= N; i++)
			parent[i] = i;

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				int check = Integer.parseInt(st.nextToken());
				if (i == j)
					continue;
				if (check == 1)
					union(i, j);
			}
		}

		st = new StringTokenizer(br.readLine());
		int cityA = Integer.parseInt(st.nextToken()); // 시작도시
		for (int i = 1; i < M; i++) {
			int cityB = Integer.parseInt(st.nextToken());
			if (checkSame(cityA, cityB) == false) {
				System.out.println("NO");
				return;
			}
			cityA = cityB;

		}
		System.out.println("YES");

	}

	private static boolean checkSame(int a, int b) {
		a = find(a);
		b = find(b);
		if (a == b)
			return true;
		return false;
	}

	private static int find(int a) {
		if (a == parent[a])
			return a;
		return parent[a] = find(parent[a]);
	}

	private static void union(int i, int j) {
		i = find(i);
		j = find(j);
		if (i != j)
			parent[i] = j;
	}

}
