package boj_23_03_14;

import java.util.Scanner;

public class B_2750_수정렬하기_합병 {

	static int[] buff;
	
	private static void mergeSort(int[] arr, int start, int N) {
		buff = new int[N];

		__mergeSort(arr, start, N - 1);

		buff = null;
	}

	private static void __mergeSort(int[] arr, int start, int end) {

		if (start >= end)
			return;

		int center = (start + end) / 2;

		__mergeSort(arr, start, center);
		__mergeSort(arr, center + 1, end);

		int buffTempIndex = 0;
		int buffCompareIndex = 0;
		int leftIndex = start;
		int i = start;

		while (i <= center) {
			buff[buffTempIndex++] = arr[i++];
		}

		while (leftIndex < end && buffCompareIndex < buffTempIndex) {
			arr[leftIndex++] = (buff[buffCompareIndex] <= arr[i]) ? buff[buffCompareIndex++] : arr[i++];
		}

		while (buffCompareIndex < buffTempIndex)
			arr[leftIndex++] = buff[buffCompareIndex++];

	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int[] arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		
		mergeSort(arr, 0, N);
		
		for (int i = 0; i < N; i++) {
			System.out.println(arr[i]);
		}

	}
}
