package boj_23_0316;

import java.util.Scanner;

public class B_1941_소문난칠공주 {

	static char[] arrComb = new char[7];
	static char[][] tableSY = new char[5][5];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		for (int i = 0; i < 5; i++) {
			String nextLine = sc.nextLine();
			for (int j = 0; j < 5; j++)
				tableSY[i][j] = nextLine.charAt(j);
		}
		
		
	}
}
