package boj_23_0313;

import java.util.Scanner;

public class B_1074_Z {

	public static long recursive(int N, int row, int column) {
		//재귀함수 탈출 조건
		if (N == 1) {
			if (row == 0 && column == 0) return 0;
			if (row == 0 && column == 1) return 1;
			if (row == 1 && column == 0) return 2;
			if (row == 1 && column == 1) return 3;
				return 0;
		}

		int a = N-1;
		long quarterLength = (long)Math.pow(2,a); //4등분 사각형의 가로세로 길이
		int location = 0; // 0123번째 4등분 사각형 중 어디에 위치해있는지
		
		if (row < quarterLength && column < quarterLength) {
			location = 0;
		}
		else if (row < quarterLength && column >= quarterLength) {
			location = 1;
			column -= quarterLength;
		}
		else if (row >= quarterLength && column < quarterLength) {
			location = 2;
			row -= quarterLength;
		}
		else if (row >= quarterLength && column >= quarterLength) {
			location = 3;
			row -= quarterLength;
			column -= quarterLength;
		}
		return (long)Math.pow(quarterLength, 2) * (location) + recursive(a, row, column);
		
	}// end recursive

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int r = sc.nextInt();
		int c = sc.nextInt();

		long ans = recursive(N, r, c);
		System.out.println(ans);
	}// end main

}
