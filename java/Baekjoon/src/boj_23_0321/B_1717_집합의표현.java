package boj_23_0321;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_1717_집합의표현 {

	private static int N, M;
	private static int[] parentNode;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		parentNode = new int[N + 1];

		for (int i = 0; i <= N; i++) {
			parentNode[i] = i;
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int question = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			if (question == 0)
				union(a, b);
			else {
				if (checkSame(a, b))
					System.out.println("YES");
				else
					System.out.println("NO");
			}
		}

	}

	private static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a != b) {
			parentNode[b] = a;
		}
	}

	private static int find(int a) { // index와 값이 같은 노드(집합의 대표 노드)를 찾아감.
		if (a == parentNode[a])
			return a;
		return parentNode[a] = find(parentNode[a]);
	}

	private static boolean checkSame(int a, int b) {
		a = find(a);
		b = find(b);
		if (a == b) {
			return true;
		}
		return false;
	}

}
