package boj_23_03_15;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class B_9742_순열 {

	private static long[] arrFactorial;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb;

		// 팩토리얼 저장한 배열
		arrFactorial = new long[12];
		arrFactorial[1] = 1;
		for (int i = 2; i <= 11; i++)
			arrFactorial[i] = arrFactorial[i - 1] * i;

		String newLine = "";
		while (true) {
			sb = new StringBuilder();
			newLine = br.readLine();
			if (newLine == null) break;
			st = new StringTokenizer(newLine);

			char[] arrCharNewLine = st.nextToken().toCharArray();
			int len = arrCharNewLine.length;
			LinkedList<Character> listChar = new LinkedList<>();
			for (int i = 0; i < len; i++) {
				listChar.add(arrCharNewLine[i]);
			}
			int k = Integer.parseInt(st.nextToken());

			sb.append(arrCharNewLine).append(' ').append(k).append(" = ");
			k--; // k가 0일 때 1번째 순열이기 때문에
			if (k+1 > arrFactorial[len]) {
				sb.append("No permutation\n");
				System.out.print(sb);
				continue;
			}

			for (int i = len - 1; i >= 1; i--) {
				long factorial = arrFactorial[i];
				int order = (int)(k / factorial);
				k %= factorial;
				
				sb.append(listChar.get(order));
				listChar.remove(order);
			}
			sb.append(listChar.get(0)).append('\n');
			System.out.print(sb);
		}
	}

}
