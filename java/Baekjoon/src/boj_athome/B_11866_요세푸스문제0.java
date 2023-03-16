package boj_athome;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B_11866_요세푸스문제0 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int N = sc.nextInt();
		int K = sc.nextInt();
		Queue<Integer> queue1 = new LinkedList<>();
		
		for (int i = 1; i <= N; i++) {
			queue1.add(i);
		}
		
		sb.append('<');
		while (queue1.size() != 1) {
			for (int i = 1; i < K; i++) {
				queue1.add(queue1.poll());
			}
			sb.append(queue1.poll()).append(", ");
		}
		sb.append(queue1.poll()).append('>');
		System.out.println(sb);

	}

}
