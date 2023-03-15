package boj_23_03_15;
조합으로 다시 만들어야됨
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_1759_암호만들기 {

	private static int L, C;
	private static char[] arrChar;
	private static boolean[] visited;
	private static char[] keyCombination;
	private static StringBuilder sb;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());

		arrChar = new char[C];
		for (int i = 0; i < C; i++)
			arrChar[i] = st.nextToken().charAt(0);

		visited = new boolean[C];
		keyCombination = new char[L];

		permutation(0, 1);

	}

	private static void permutation(int N, int a) {
		if (N == L) {
			for (int i = 0; i < L; i++)
				System.out.print(keyCombination[i]);
			System.out.println();
			return;
		}

		for (int i = a; i < C; i++) {
			if (visited[i] == true)
				continue;
			keyCombination[N] = arrChar[i];
			visited[i] = true;
			permutation(N + 1, a + 1);
			visited[i] = false;
		}

	}
}
