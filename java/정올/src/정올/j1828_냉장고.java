package 정올;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class j1828_냉장고 {
	
	private static int N;
	private static int[][] substances;
	private static boolean[] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		substances = new int[N][2];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			substances[i][0] = Integer.parseInt(st.nextToken());
			substances[i][1] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(substances, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[1] - o2[1] == 0)
					return o1[0] - o2[0];
				return o1[1] - o2[1];
			}
			
		}); // 최고보관온도 기준으로 정렬, 같을 경우 최저보관온도 기준으로.
		
		
		int fridgeTemperature = 0;
		int fridgeCount = 0;
		visited = new boolean[N];
		
		for (int i = 0; i < N; i++) {
			fridgeTemperature = substances[i][1];
			if (visited[i]==true)
				continue; //이미 저장할 냉장고가 정해졌으면 다음 물질로 넘어간다.
			visited[i] = true; // i번째 물질은 저장할 냉장고가 있음.
			fridgeCount++; //아직 저장할 냉장고가 정해지지 않은 물질일 경우 냉장고 개수를 하나 더 올려준다.
			
			for (int j = i; j < N; j++) {
				if (substances[j][0] <= fridgeTemperature)
					visited[j] = true;
			}
		}
		
		System.out.println(fridgeCount);
		
	}

}
