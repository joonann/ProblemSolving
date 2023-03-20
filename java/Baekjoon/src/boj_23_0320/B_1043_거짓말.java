package boj_23_0320;
ㅇㅇㅇ
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_1043_거짓말 {

	private static int N, M; // 사람 수, 파티 개수
	private static int countKnowsTruth;
	private static int[] personKnowsTruth;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		countKnowsTruth = Integer.parseInt(st.nextToken());
		personKnowsTruth = new int[countKnowsTruth + 1];

	}

}
