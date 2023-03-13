package B_23_03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B_2018_수들의합5 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int start_index = 1;
		int end_index = 1;
		int sum = 0, count = 0;

		while (true) {
			if (end_index > N)
				break;
			for (; sum <= N; end_index++) {
				sum += end_index;
				if (sum == N)
					count++;
			}
			for (; sum >= N; start_index++) {
				sum -= start_index;
				if (sum == N)
					count++;
			}
		}
		System.out.println(count);
	}

}
