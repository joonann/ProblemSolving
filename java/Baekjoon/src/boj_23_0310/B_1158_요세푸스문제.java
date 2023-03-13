package boj_23_0310;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B_1158_요세푸스문제 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		Queue<Integer> q1 = new LinkedList<>();
		
		for (int i = 0; i < N; i++) {
			q1.add(i+1);			
		}
		
		while (q1.size() != 0) {
			for (int i = 0; i < K - 1; i++) {
				q1.add(q1.poll());
			}
			if (q1.size() > 1)
				sb.append(q1.poll()+", ");
			else
				sb.append(q1.poll()+">");
		}
		
		System.out.println(sb);
	}

}
