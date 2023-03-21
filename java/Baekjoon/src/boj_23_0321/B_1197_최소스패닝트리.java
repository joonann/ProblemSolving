package boj_23_0321;

import java.util.PriorityQueue;
import java.util.Scanner;

public class B_1197_최소스패닝트리 {
	static int[] parent;
	static PriorityQueue<pEdge> queue;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		queue = new PriorityQueue<>();
		parent = new int[N+1];
		for (int i = 0; i < N; i++) {
			parent[i] = i;
		}
		
		for (int i = 0; i < M; i++) {
			int s = sc.nextInt();
			int e = sc.nextInt();
			int v = sc.nextInt();
			queue.add(new pEdge(s, e, v));
		}
		
		int useEdge = 0;
		int result = 0;
		while (useEdge < N -1) {
			pEdge now = queue.poll();
			if (find(now.s) != find(now.e)) {
				union(now.s, now.e);
				result = result + now.v;
				useEdge++;
			}
		}
		
		System.out.println(result);
	}

	public static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a != b) {
			parent[b] = a;
		}
	}
	
	public static int find(int a) {
		if (a == parent[a])
			return a;
		else
			return parent[a] = find(parent[a]);
	}
	
	static class pEdge implements Comparable<pEdge> {
		int s;
		int e;
		int v;
		
		pEdge(int s, int e, int v) {
			this.s = s;
			this.e = e;
			this.v = v;
		}
		
		@Override
		public int compareTo(pEdge o) {
			//가중치를 기준으로 오름차순 정렬을 하기 위해 compareTo 재정의
			return this.v - o.v;
		}
	}
	
}
