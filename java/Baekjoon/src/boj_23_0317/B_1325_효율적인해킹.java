package boj_23_0317;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class B_1325_효율적인해킹 {

	private static int N, M;
	private static ArrayList<Integer>[] computer;
	private static int[][] computerArray;
	private static boolean[] visited;
	private static int tempCount;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken()); // N 대의 컴퓨터
		M = Integer.parseInt(st.nextToken()); // M 개의 신뢰관계

		computer = new ArrayList[N+1]; //컴퓨터 ArrayList배열
		for (int i = 1; i <= N; i++) {
			computer[i] = new ArrayList<Integer>();
		} // 컴퓨터 N대를 한 대당 ArrayList 한 개로 생성.
		
		for (int i = 0; i < M; i++) { // M 개의 신뢰 관계를 ArrayList에 저장.
			st = new StringTokenizer(br.readLine());
			int trustFrom = Integer.parseInt(st.nextToken());
			int trustTo = Integer.parseInt(st.nextToken());
			
			computer[trustTo].add(trustFrom);
			// 컴퓨터 1의 ArrayList에는 컴퓨터 1을 신뢰하는 컴퓨터들의 번호를 저장한다.
			// 컴퓨터 1을 해킹한 경우 컴퓨터 1을 신뢰하는 컴퓨터들 역시 해킹할 수 있기 때문에.
		}
		
		computerArray = new int[N+1][]; // ArrayList는 get 하기에 시간이 오래걸리기 때문에 2차원 배열에 옮겨줘서 시간복잡도를 줄였음.
		for(int i = 1; i <= N; i++) {
			int size = computer[i].size();
			computerArray[i] = new int[size];
			for (int j = 0; j < size; j++) {
				computerArray[i][j] = computer[i].get(j);
			}
		}
		
		ArrayList<Integer> answer = new ArrayList<>();
		int hackingComputerMaxCount = 0;
		
		for (int i = 1; i <= N; i++) {
			visited = new boolean[N+1]; //dfs를 위한 visited배열
			tempCount = 0;
			
			DFS(i);
			
			if (hackingComputerMaxCount == tempCount)
				answer.add(i);
			else if (hackingComputerMaxCount < tempCount) {
				answer = new ArrayList<>();
				answer.add(i);
				hackingComputerMaxCount = tempCount;
			}
		}//end for
		
		int answersize = answer.size();
		for (int i = 0; i < answersize; i++)
			System.out.print(answer.get(i) + " ");
	}//end main

	private static void DFS(int start) {
		if (visited[start] == true)
			return;
		visited[start] = true;
		tempCount++;
		int length = computerArray[start].length;
		for (int i = 0; i < length; i++) {
			DFS(computerArray[start][i]);
		}
		
	}
	
	
	
	

}
