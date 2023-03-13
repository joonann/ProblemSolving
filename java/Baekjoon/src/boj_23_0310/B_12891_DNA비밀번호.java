package boj_23_0310;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_12891_DNA비밀번호 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int P = Integer.parseInt(st.nextToken()); // 전체 문자열 길이
		int S = Integer.parseInt(st.nextToken()); // 검색할 부문자열 길이

		String dna = br.readLine(); // 전체 문자열

		st = new StringTokenizer(br.readLine()); // 세 번째 줄 입력값.(필요 개수)
		int[] acgt = new int[4]; // ACGT 필요 개수

		// ACGT 최소 필요 개수
		int minA = Integer.parseInt(st.nextToken());
		int minC = Integer.parseInt(st.nextToken());
		int minG = Integer.parseInt(st.nextToken());
		int minT = Integer.parseInt(st.nextToken());

		// 첫 S개 부문자열 ACGT 각 개수 저장
		for (int i = 0; i < S; i++) {
			char dnaIndex = dna.charAt(i);

			if (dnaIndex == 'A')
				acgt[0]++;
			else if (dnaIndex == 'C')
				acgt[1]++;
			else if (dnaIndex == 'G')
				acgt[2]++;
			else if (dnaIndex == 'T')
				acgt[3]++;

		}

		int count = 0;

		// 슬라이딩 윈도우 기법 활용해서 한 칸씩 밀면서 유효한 비밀번호 개수 증가.
		for (int i = 0;; i++) {
			int endIndex = i + S;

			if (acgt[0] >= minA && acgt[1] >= minC && acgt[2] >= minG && acgt[3] >= minT)
				count++;

			if (endIndex == P)
				break;

			// window slide

			char startChar = dna.charAt(i);
			char endChar = dna.charAt(endIndex);

			if (endChar == 'A')
				acgt[0]++;
			else if (endChar == 'C')
				acgt[1]++;
			else if (endChar == 'G')
				acgt[2]++;
			else if (endChar == 'T')
				acgt[3]++;

			if (startChar == 'A')
				acgt[0]--;
			else if (startChar == 'C')
				acgt[1]--;
			else if (startChar == 'G')
				acgt[2]--;
			else if (startChar == 'T')
				acgt[3]--;

		} // end for

		System.out.println(count);

	}// end main

}
