package B_23_03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_11660_구간합구하기5 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken()) + 1;
		int M = Integer.parseInt(st.nextToken());
		int[][] arr = new int[N][N];
		int[][] dp = new int[N][N]; //여기를 더 줄여도 되겠다
		
		for (int i = 1; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 1; i < N; i++) {
			for (int j = 1; j < N; j++) {
				dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+arr[i][j];
			}
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			System.out.println(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]);
		}
		
	}

}
