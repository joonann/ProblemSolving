package boj_23_03_14;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class B_9742_순열 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());

		int[] cord = new int[10];
		String s1 = st.nextToken();
		int N = Integer.parseInt(st.nextToken());
		LinkedList<Character> arrChar = new LinkedList<>();

		int[] factorials = new int[11];
		factorials[1] = 1;
		for (int i = 2; i <= 10; i++) {
			factorials[i] = factorials[i - 1] * i;
		}

		// arrList.remove(index)
		// LinkedList.remove(index)

		int len = s1.length();

		for (int i = len; i > 0; i++) {
			int branch = N / i;
			N %= i;

		}

	}

}
