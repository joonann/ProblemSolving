package boj_23_0317;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class B_13023_친구관계파악하기 {

	private static int N, M;
	private static ArrayList<Integer>[] personN;
	private static int answer;
	private static boolean[] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		personN = new ArrayList[N];
		for (int i = 0; i < N; i++) {
			personN[i] = new ArrayList<Integer>();
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			personN[a].add(b);
			personN[b].add(a);
		}

		answer = 0;
		visited = new boolean[N];
		for (int i = 0; i < N; i++) {
			DFS(i, 0);
		}
		System.out.println(answer);
	}

	private static void DFS(int start, int depth) {
		if (answer == 1)
			return;
		if (depth == 3) {
			for (int i = 0; i < personN[start].size(); i++) {
				int a = personN[start].get(i);
				if (visited[a] == false) {
					answer = 1;
					return;
				}
			}
			return; 
		}
		visited[start] = true;
		for (int i = 0; i < personN[start].size(); i++) {
			int a = personN[start].get(i);
			if (visited[a] == false)
			DFS(a, depth+1);
		}
		visited[start] = false;
		return;
	}
	
	

}
