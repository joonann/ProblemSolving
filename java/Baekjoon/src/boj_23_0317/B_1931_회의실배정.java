package boj_23_0317;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class B_1931_회의실배정 {

	private static int N;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		int[][] timeTable = new int[N][2];
		
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			timeTable[i][0] = Integer.parseInt(st.nextToken());
			timeTable[i][1] = Integer.parseInt(st.nextToken());
			
		}
		
		Arrays.sort(timeTable, new Comparator<int[]>() {

			@Override
			public int compare(int[] S, int[] E) {
				if (S[1] == E[1])
					return S[0] - E[0]; // 종료시간이 같으면 시작시간을 이용해서 정렬
				return S[1] - E[1]; // 종료시간이 다르면 종료시간을 이용해 정렬
			}
		});
		
		int count = 0;
		int end = -1;
		for (int i = 0; i < N; i++) {
			if (timeTable[i][0]>=end) { // 3시에 끝나고 3시에 시작할 수도 있으니까
				end = timeTable[i][1];
				count++;
			}
		}
		
		System.out.println(count);
		
	}

}
