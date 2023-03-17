	package boj_23_0316;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


//재귀(스택)을 이용해서 구현한 dfs
public class B_11724_연결요소의개수 {

	private static int N, M;
	private static ArrayList<Integer>[] arrNode;
	private static boolean visited[];
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arrNode = new ArrayList[N+1];
		visited = new boolean[N+1];
		
		arrNode[0] = new ArrayList<Integer>();
		for (int i = 1; i <= N; i++) {
			arrNode[i] = new ArrayList<Integer>();
		}
		
		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			
			arrNode[start].add(end);
			arrNode[end].add(start);
		}
		
		int count = 0;
		
		for (int i = 1; i <= N; i++) {
			if (visited[i] == false) {
				count++;
				DFS(i);
			}
				
		}
		System.out.println(count);
		
	}
	private static void DFS(int i) {
		if (visited[i] == true)
			return;
		visited[i] = true;
		for (int a : arrNode[i]) {
			if (visited[a] == false)
				DFS(a);
		}
	}
	

}
