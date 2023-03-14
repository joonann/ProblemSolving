package boj_23_0313;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B_1940_주몽 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());

		int[] arrInput = new int[N]; // 각 재료 숫자 배열

		for (int i = 0; i < N; i++)
			arrInput[i] = Integer.parseInt(st.nextToken());

		
		Arrays.sort(arrInput);
		
		int firstP = 0;
		int secondP = N-1;
		int sum = 0;
		int count = 0;
		
		while (firstP < secondP) {
			sum = arrInput[firstP] + arrInput[secondP];
			if (sum == M) {
				count++;
				firstP++;
			}
			else if (sum < M) {
				firstP++;
			}
			else
				secondP--;
		}
		System.out.println(count);
	}
}
