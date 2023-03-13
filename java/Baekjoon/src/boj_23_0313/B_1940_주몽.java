package boj_23_0313;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_1940_주몽 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());

		int[] arrInput = new int[N]; // 각 재료 숫자 배열

		int maxInputOrM = M;

		for (int i = 0; i < N; i++) {
			arrInput[i] = Integer.parseInt(st.nextToken());
			if (maxInputOrM < arrInput[i])
				maxInputOrM = arrInput[i];
		}

		int[] arrHowManyM = new int[maxInputOrM + 1]; // 각 재료의 개수 배열

		for (int i = 0; i < N; i++) {
			arrHowManyM[arrInput[i]]++;
		}

		int sum = 0;
		for (int i = 1; i <= (M / 2); i++) {
			sum += Math.min(arrHowManyM[i], arrHowManyM[M - i]);
		}

		System.out.println(sum);
	}

}
