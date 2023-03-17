package boj_23_03_15;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B_1759_암호만들기 {

	private static int L, C;
	private static char[] arrChar;
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

		Arrays.sort(arrChar);

		keyCombination = new char[L];

		combination(0, 0);

	}

	private static void combination(int N, int a) {
		if (N == L) {
			int aeiou = 0;
			for (int i = 0; i < L; i++) {
				char check = keyCombination[i];
				switch (check) {
				case 'a':
				case 'e':
				case 'i':
				case 'o':
				case 'u':
					aeiou++;
				}
			}
			if (aeiou < 1) return;
			if (aeiou > L - 2) return;
			for (int i = 0; i < L; i++)
				System.out.print(keyCombination[i]);
			System.out.println();
			return;
		}
		for (int i = a; i < C; i++) {
			keyCombination[N] = arrChar[i];
			combination(N + 1, i + 1);
		}

	}
}
