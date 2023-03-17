package boj_23_0317;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B_1931_회의실배정_객체활용 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		Meeting timeTable[] = new Meeting[N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			timeTable[i] = new Meeting(start, end);
		}

		Arrays.sort(timeTable); // comparable<> 인터페이스를 구현한 Meeting 클래스의 compareTo 메서드의 규칙에 따라 정렬.

		int count = 0;
		int beforeEnd = -1;

		for (int i = 0; i < N; i++) {
			if (timeTable[i].start >= beforeEnd) {
				beforeEnd = timeTable[i].end;
				count++;
			}
		}
		System.out.println(count);

	}

	private static class Meeting implements Comparable<Meeting> {
		private int start;
		private int end;

		public Meeting(int start, int end) {
			super();
			this.start = start;
			this.end = end;
		}

		@Override
		public int compareTo(Meeting o) {
			if (this.end == o.end) {
				return this.start - o.start;
			}
			return this.end - o.end;
		}
	}
}
