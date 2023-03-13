package boj_23_0313;

import java.util.Scanner;

public class B_2750_수정렬하기_선택 {

	public static void swap(int[] arr, int i, int j) {
		int temp;
		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int[] arr = new int[N];
		
		for (int i = 0; i < N-1; i++) {
			arr[i] = sc.nextInt();
		}
		
		for (int i = 0; i < N; i++) {
			int minIdx = i;
			for (int j = i; j < N; j++) {
				if (arr[minIdx] > arr[j])
					minIdx = j;
			}				
			
			swap(arr, i, minIdx);
		}
		
		for (int i = 0; i < N; i++) {
			System.out.println(arr[i]);
		}

	}

}
