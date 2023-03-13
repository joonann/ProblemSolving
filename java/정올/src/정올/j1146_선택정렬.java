package 정올;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class j1146_선택정렬 {

	public static void swap(int[] arr, int i, int j) {
		int t = arr[i];
		arr[i] = arr[j];
		arr[j] = t;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		int[] arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < N-1; i++) {
			int minIndex = i;
			for (int j = i + 1; j < N; j++) {
				if (arr[minIndex] > arr[j])
					minIndex = j;
			}
			swap(arr, i, minIndex);
			for (int j=0; j<N-1; j++)
				System.out.print(arr[j]+" ");
			System.out.println(arr[N-1]);
		}
		
	}

}
