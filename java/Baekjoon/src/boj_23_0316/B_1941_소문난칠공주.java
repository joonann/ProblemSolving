package boj_23_0316;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B_1941_소문난칠공주 {

	static int[] arrCombIndex = new int[7]; // 인덱스를 조합 배열에 담아줘서 S의 개수와 인접 여부를 확인해볼 것.
	static char[] tableSY = new char[49]; // 1~5, 6~10, 11~15, 16~20, 21~25
											// 나눠서 2차원 배열을 1차원 배열로 생각해서 저장.
	static int[] possibleIndex = new int[25]; // 헷갈리지 않게 가능한 index 번호들을 모아둔 int 배열(조합 함수에서 사용)
	static int answer = 0; // S개수를 확인하고 인접 여부를 판단해 답을 증가시켜줌.

	static boolean[] visited; // 조합이 정해진 뒤 7개의 인덱스를 true로 바꿔줌
	static boolean[] BFSvisited; // BFS 탐색할 때 사용할 visited 배열
	static Queue<Integer> queue; // BFS 탐색할 때 사용할 큐

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int index = 0;
		for (int i = 1; i <= 5; i++) {
			String nextLine = sc.nextLine();
			for (int j = 1; j <= 5; j++) {
				tableSY[i * 7 + j] = nextLine.charAt(j - 1);
				possibleIndex[index++] = i * 7 + j;
			}
		}

//		0000000    0  1  2  3  4  5  6
//		0YSYSY0    7  8  9 10 11 12 13
//		0SYSYS0   14 15 16 17 18 19 20
//		0YSYSY0   21 22 23 24 25 26 27
//		0SYSYS0   28 29 30 31 32 33 34
//		0YSYSY0   35 36 37 38 39 40 41
//		0000000   42 43 44 45 46 47 48
//		
//		25개의 index = 8 9 10 11 12, 15 16 17 18 19, 22 23 24 25 26, 29 30 31 32 33, 36 37 38 39 40
//		와 같은 2차열 배열을 1차원 형태로 이어붙인 배열에 옮겨주었다.
//		+5 -5 -1 +1 연산을 통해 상하좌우의 값 확인 가능.
//		0,0 번째 앉은 사람의 인덱스 : 8

		combination(0, 0);
		System.out.println(answer);
	}

	private static void combination(int n, int start) { // 25개의 가능한 인덱스 중 7개를 인덱스 조합을 구해준다.
		
		// 1. 재귀함수를 통해 조합 7개를 완성한 경우
		if (n == 7) { 
			
			// 2. S파가 4명 이상인지 확인하고
			if (combCountS(arrCombIndex) >= 4) {  
				
				visited = new boolean[49];
				for (int i = 0; i < 7; i++) {
					visited[arrCombIndex[i]] = true;
				}
				int startIndex = arrCombIndex[0];

				
				// 3. 가로세로로 이어져있는지 확인해서
				if (BFSisLinked(startIndex) == false)  
					return;
				
				// 4. answer를 하나씩 증가시켜준다.
				answer++; 
			}
			return;
		}
		for (int i = start; i < 25; i++) {
			arrCombIndex[n] = possibleIndex[i];
			combination(n + 1, i + 1);
		}
	}

	private static int combCountS(int[] arrayIndex) { // 7개의 조합에서 S의 개수를 세어 반환하는 함수
		int count = 0;
		for (int a : arrayIndex) {
			if (tableSY[a] == 'S')
				count++;
		}
		return count;
	}

	private static boolean BFSisLinked(int start) { // 7개의 노드가 start 자리부터 시작해서 이어져있는지 확인하는 BFS 탐색 함수
		int count = 1; // start와 연결돼있는 노드 개수를 구해서 7이라면 true를 반환할 것.
		BFSvisited = new boolean[49];
		BFSvisited[start] = true;
		queue = new LinkedList<>();
		queue.add(start);
		while (queue.isEmpty() == false) {
			int next_node = queue.poll();
			if (visited[next_node - 1] == true && BFSvisited[next_node - 1] == false) { // 왼쪽 자리 탐색
				BFSvisited[next_node - 1] = true;
				queue.add(next_node - 1);
				count++;
			}
			if (visited[next_node + 1] == true && BFSvisited[next_node + 1] == false) { // 오른쪽 자리 탐색
				BFSvisited[next_node + 1] = true;
				queue.add(next_node + 1);
				count++;
			}
			if (visited[next_node - 7] == true && BFSvisited[next_node - 7] == false) { // 위쪽 자리 탐색
				BFSvisited[next_node - 7] = true;
				queue.add(next_node - 7);
				count++;
			}
			if (visited[next_node + 7] == true && BFSvisited[next_node + 7] == false) { // 아래쪽 자리 탐색
				BFSvisited[next_node + 7] = true;
				queue.add(next_node + 7);
				count++;
			}
		}
		if (count == 7) return true;
		return false;
	}
	
}
