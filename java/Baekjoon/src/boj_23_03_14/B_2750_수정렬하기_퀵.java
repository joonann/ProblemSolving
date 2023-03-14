package boj_23_03_14;
ㅇㅇㅇ
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class B_2750_수정렬하기_퀵 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int[] arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		
		quickSort(arr, 0, N);
		
		for (int i = 0; i < N; i++) {
			System.out.println(arr[i]);
		}

	}

	private static void quickSort(int[] arr, int i, int n) {
		
		
	}

}
