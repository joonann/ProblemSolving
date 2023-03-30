package boj_23_0330;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B_15686_치킨배달 {

	private static int N, M, bbqCount, homeCount;
	private static int minDistance = 0;
	private static int[][] newMap;
	private static ArrayList<Location> bbqList = new ArrayList<>();
	private static ArrayList<Location> homeList = new ArrayList<>();
	private static int[] combIndex; // 인덱스 M개
	private static boolean[][] visited;

	private static class Location {
		int row;
		int column;

		Location(int i, int j) {
			this.row = i;
			this.column = j;
		}
	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		newMap = new int[N + 1][N + 1];
		combIndex = new int[M];

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				int temp = Integer.parseInt(st.nextToken());
				newMap[i][j] = temp;
				if (temp == 1) {
					homeList.add(new Location(i, j));
				} else if (temp == 2) {
					newMap[i][j] = 0;
					bbqList.add(new Location(i, j));
				}
			}
		}
		bbqCount = bbqList.size();
		homeCount = homeList.size();
//		0, 1, 2 ... 치킨집수-1 까지 인덱스에서 combination
// 		combination 이후 bfs
//		minDistance보다 커지면 백트래킹, 		

		combination(0, 0);

	}

	private static void combination(int start, int depth) {
		if (depth == M) {
			drawBbqMap();
			bfs();
			eraseBbqMap();
			return;
		}
		for (int i = start; i < bbqCount; i++) {
			combIndex[depth] = i;
			combination(i + 1, depth + 1);
		}
	}

	private static void drawBbqMap() {
		for (int i = 0; i < combIndex.length; i++)
			newMap[bbqList.get(i).row][bbqList.get(i).column] = 2;
	}

	private static void eraseBbqMap() {
		for (int i = 0; i < combIndex.length; i++)
			newMap[bbqList.get(i).row][bbqList.get(i).column] = 0;
	}

	private static boolean foundBbq(Location location) {
		if (newMap[location.row][location.column] == 2)
			return true;
		return false;
	}

	private static void bfs() {
		int tempDistance = 0;
		Location myHome;
		Queue<Location> queue = new LinkedList<>(); 
		
		
		for (int i = 0; i < homeList.size(); i++) {
			if (tempDistance > minDistance)
				return;
			myHome = homeList.get(i);
			visited = new boolean[N+1][N+1];
			int myBbqDistance = 0;
			queue.add(myHome);
			
			while (true) {
				myBbqDistance++;
				if (queue.isEmpty())
			}
			tempDistance += myBbqDistance; 
		}
		minDistance = tempDistance;
	}

}
