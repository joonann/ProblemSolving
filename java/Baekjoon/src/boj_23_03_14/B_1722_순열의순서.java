package boj_23_03_14;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class B_1722_순열의순서 {

	public static long[] arrFactorial; // i번째 index에는 i!가 저장되어 있음.
	public static LinkedList<Integer> usingNumbers; // 사용할 숫자들이 담긴 연결 리스트

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		// 정적으로 선언한 팩토리얼 배열에 팩토리얼 값 / 연결 리스트에 사용할 숫자들 저장.
		arrFactorial = new long[N + 1];
		arrFactorial[1] = 1;
		usingNumbers = new LinkedList<>();
		usingNumbers.add(1);
		for (int i = 2; i <= N; i++) {
			arrFactorial[i] = arrFactorial[i - 1] * i;
			usingNumbers.add(i);
		}

		StringTokenizer st = new StringTokenizer(br.readLine());

		// 문제 넘버에 따른 메서드 구분.(1 또는 2)
		int problemNumber = Integer.parseInt(st.nextToken());
		if (problemNumber == 1) {
			long k = Long.parseLong(st.nextToken());

			// 1번 문제일 경우 N과 K를 이용해 K번째 순열을 출력하는 메서드 호출
			problemOne(N, k - 1);

		} else if (problemNumber == 2) {
			int[] dest = new int[N];
			for (int i = 0; i < N; i++)
				dest[i] = Integer.parseInt(st.nextToken());

			// 2번 문제일 경우 N과 dest순열을 이용해 dest 순열의 순번을 출력하는 메서드 호출
			problemTwo(N, dest);

		}
	}// end main

	private static void problemOne(int N, long k) {

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < N; i++) {
			long factorial = arrFactorial[N - 1 - i]; // 하나 작은 팩토리얼 값으로 나눠서 순서를 찾음
			int order;
			if (factorial == 0)
				order = (int) k;
			else {
				order = (int) (k / factorial);
				k = k % factorial;
			}

			sb.append(usingNumbers.get(order)).append(' ');
			usingNumbers.remove(order);

		}

		System.out.println(sb.toString());

	}// end problemOne

	private static void problemTwo(int N, int[] dest) {
		long ans = 1;

		for (int i = 0; i < N; i++) {
			int order = 0;
			int restSize = usingNumbers.size();
			while (order < restSize) {
				if (dest[i] == usingNumbers.get(order))
					break;
				order++;
			}

			ans += arrFactorial[N - 1 - i] * (long) (order);
			usingNumbers.remove(order);

		}

		System.out.println(ans);

	}// end problemTwo

}
