package boj_23_0310;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class B_2493_탑 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();

		Stack<Integer> s1 = new Stack<>();
		Stack<Integer> stackIndex = new Stack<>();
		
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = 0; i < N; i++) {
			int height = arr[i];

			while (s1.size() != 0) {
				int peek = s1.peek();
				if (peek < height) {
					s1.pop();
					stackIndex.pop();
				} else if (peek > height) {
					sb.append(stackIndex.peek()).append(' ');
					s1.push(height);
					stackIndex.push(i+1);
					break;
				}

			}// end while

			if (s1.size() == 0) {
				s1.push(height);
				stackIndex.push(i+1);
				sb.append(0).append(' ');
			}

		}// end for
		
		sb.deleteCharAt(sb.length()-1);
		System.out.println(sb);
	}// end main

}
