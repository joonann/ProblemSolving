package boj_23_0321;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_2609_최대공약수와최소공배수 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int GCD = 1; // great common divisor
		int LCM = 1;// least common multiple
		
		int small = Math.min(N,  M);
		
		// 최대공약수를 구하기 위해 작은 숫자까지 모든 자연수로 공약수들을 찾아본다.
		int CD = 1;
		for (CD = 1; CD <= small; CD++) {
			if (N%CD == 0 && M%CD == 0) {
				GCD = CD;
			}
		}
		
		int tempN = N / GCD;
		int tempM = M / GCD;
		
		LCM = GCD * tempN * tempM;
		
		System.out.println(GCD);
		System.out.println(LCM);
		
				
	}

}
