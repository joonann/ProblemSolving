package boj_23_0316;
복습ㄱㄱㄱ
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B_1260_DFSBFS {

	private static int N, M, Start;
	private static ArrayList<Integer>[] arrNode;
	private static boolean visited[];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		Start = Integer.parseInt(st.nextToken());
		arrNode = new ArrayList[N + 1];
		visited = new boolean[N + 1];
//		arrNode[0] = new ArrayList<Integer>(); // 굳이 안 해도 됨
//		visited[0] = false; // 굳이 안 해도 됨

		for (int i = 1; i <= N; i++) {
			arrNode[i] = new ArrayList<Integer>();
		}

		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(br.readLine());
			int from, to;
			from = Integer.parseInt(st.nextToken());
			to = Integer.parseInt(st.nextToken());
			arrNode[from].add(to);
			arrNode[to].add(from);
		}

		// 방문할 수 있는 노드가 여러 개일 경우에는 번호가 작은 것을 먼저 방문하기 위해 정렬하기
		for (int i = 1; i <= N; i++) {
			Collections.sort(arrNode[i]);
		}
		visited = new boolean[N + 1];
		DFS(Start);
		System.out.println();
		visited = new boolean[N + 1];
		BFS(Start);
		System.out.println();

	}

	private static void DFS(int node) { // DFS 구현
		System.out.print(node + " ");
		visited[node] = true;
		for (int i : arrNode[node]) {
			if (visited[i] == false)
				DFS(i);
		}
	}

	private static void BFS(int node) { // BFS 구현
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(node);
		visited[node] = true;

		while (queue.isEmpty() == false) {
			int now_node = queue.poll();
			System.out.print(now_node + " ");
			for (int i : arrNode[now_node]) {
				if (visited[i] == false) {
					visited[i] = true;
					queue.add(i);
				}
			}
		}
	}

}
