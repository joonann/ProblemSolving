package boj_23_0313;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_24090_퀵정렬1 {

	static int recordK = 0;
	static int K = 0;

	public static void swap(int[] A, int i, int j) {
		int temp = A[i];
		A[i] = A[j];
		A[j] = temp;
		recordK++;
		if (recordK == K)
			System.out.println(A[i] + " " + A[j]);
	}

	public static void quickSort(int[] A, int p, int r) {
		if (p < r) {
			int q = partition(A, p, r);
			quickSort(A, p, q - 1);
			quickSort(A, q + 1, r);
		}
	}

	public static int partition(int[] A, int p, int r) {
		int x = A[r];
		int i = p - 1;
		for (int j = p; j <= r - 1; j++) {
			if (A[j] <= x) {
				swap(A, ++i, j);
			}
		}
		if (i + 1 != r) {
			swap(A, i + 1, r);
		}
		return i + 1;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());

		int[] arr = new int[N];

		for (int i = 0; i < N; i++)
			arr[i] = Integer.parseInt(st.nextToken());

		quickSort(arr, 0, N - 1);

		if (recordK < K)
			System.out.println(-1);
	}

}
