package boj_23_0310;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class B_1874_스택수열 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Integer> s1 = new Stack<>();

		// +와-를 한 번에 StringBuilder에 붙여주고 NO가 아닐 경우 출력.
		StringBuilder sb = new StringBuilder();

		int n = Integer.parseInt(br.readLine()); // 입력값 개수
		int[] arrInput = new int[n];

		// 입력값 배열에 저장
		for (int i = 0; i < n; i++) {
			arrInput[i] = Integer.parseInt(br.readLine());
		}

		int indexInput = 0;// 입력값 배열 인덱스 (순서대로 pop할 예정)
		int number = 1;// 스택에 push하는 숫자 (1,2,3,...)
		for (int i = 0; i < n; i++) { // n 번의 push를 진행할 것.

			// 현재 push하는 숫자와 pop해야하는 숫자가 같으면 push하고 바로 pop
			if (number == arrInput[indexInput]) {
				s1.push(number);
				sb.append("+\n");
				number++;
				s1.pop();
				sb.append("-\n");
				indexInput++;

				// pop한 다음 숫자도 연달아 pop 가능할 경우 계속 pop
				while (!s1.isEmpty()) {
					if (s1.peek() != arrInput[indexInput])
						break;
					s1.pop();
					sb.append("-\n");
					indexInput++;
				}
			}
			// 현재 push하는 숫자가 pop할 숫자보다 작으면 push
			else if (number < arrInput[indexInput]) {
				s1.push(number);
				sb.append("+\n");
				number++;

			}
		}
		if (s1.size() == 0) // 모든 stack 안의 숫자를 pop했을 경우
			System.out.println(sb); // StringBuilder.toString 출력
		else
			System.out.println("NO"); // 입력된 수열을 만들 수 없는 경우 NO 출력

	}// end main

}
