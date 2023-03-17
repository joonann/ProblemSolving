package boj_23_0316;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_10915_덧셈 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		String newLine;
		
		while ((newLine = br.readLine()) != null) {
			int a, b;
			
			st = new StringTokenizer(newLine);
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			System.out.println(a+b);
		}

	}

}
