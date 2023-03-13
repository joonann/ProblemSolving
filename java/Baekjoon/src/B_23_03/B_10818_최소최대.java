package B_23_03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_10818_최소최대 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int Min = 1000001;
		int Max = -1000001;
		for (int i = 0; i < N; i++) {
			int eachInt = Integer.parseInt(st.nextToken());
			if (eachInt < Min) Min = eachInt;
			if (eachInt > Max) Max = eachInt;
		}
		
		System.out.println(Min+" "+Max);
				
	}

}
