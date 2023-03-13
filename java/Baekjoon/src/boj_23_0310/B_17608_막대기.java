package boj_23_0310;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_17608_막대기 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int index = N - 1;
		int	highest = 0;
		int count = 0;
		for (int i = 0; i < N; i++) {
			int height = arr[index - i];
			if (highest < height) {
				highest = height;
				count++;
			}
		}
		System.out.println(count);
	}

}
