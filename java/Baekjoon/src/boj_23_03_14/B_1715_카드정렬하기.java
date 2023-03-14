package boj_23_03_14;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;



정렬한 다음 더하면서 계속 최솟값 두개를 더하는 식으로 해야됨!

public class B_1715_카드정렬하기 {

	static int[] buff;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] arr = new int[N];
		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();

		mergeSort(arr, 0, N);

		long sum = 0;

		// 두 개씩 더해서 저장할 큐
		Queue<Long> q1 = new LinkedList<>();
		Queue<Long> q2 = new LinkedList<>();
		boolean flag = true;

		for (int i = 0; i < arr.length; i++) {
			q1.add((long) arr[i]);
		}

		while (true) {

			if (flag == true) {
				if (q1.size() == 1)
					break;
				while (q1.size() != 0) {
					if (q1.size() == 1) {
						q2.add(q1.poll());
						break;
					}
					long addNumber = q1.poll() + q1.poll();
					sum += addNumber;
					q2.add(addNumber);
				}
				flag = false;
			} 
			else if (flag == false) {
				if (q2.size() == 1)
					break;
				while (q2.size() != 0) {
					if (q2.size() == 1) {
						q1.add(q2.poll());
						break;
					}
					
					long addNumber = q2.poll() + q2.poll();
					sum += addNumber;
					q1.add(addNumber);
				}
				flag = true;
			}
		}
		System.out.println(sum);

	}

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

		while (i <= end && buffCompareIndex < buffTempIndex) {
			arr[leftIndex++] = (buff[buffCompareIndex] <= arr[i]) ? buff[buffCompareIndex++] : arr[i++];
		}

		while (buffCompareIndex < buffTempIndex)
			arr[leftIndex++] = buff[buffCompareIndex++];

	}
}
