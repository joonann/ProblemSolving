package 정올;

import java.util.Scanner;

public class j1338_문자삼각형1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		char firstChar = 'A';
		int diff = n - 1;
		

		char[][] arr = new char[n][n];
		for (int i = 0; i < n; i++) {
			int lineDiff = 0;
			for (int j = 0; j < n; j++) {
				
				if (i + j < n - 1) {
					arr[i][j] = ' ';
				} else {
					arr[i][j] = (char)(firstChar+lineDiff);
					lineDiff += diff;
				}
			} // end for
			if (firstChar == 'Z')
				firstChar = 'A' - 1;
			firstChar++;
		} // end for

		
		
		// 출력 부분 
		for (char[] cs : arr) {
			for (int i = 0; i < n; i++) {
				System.out.print(cs[i]);
				if (i < n - 1)
					System.out.print(" ");
			} // end for
			System.out.println();
		} // end for

	}
}
