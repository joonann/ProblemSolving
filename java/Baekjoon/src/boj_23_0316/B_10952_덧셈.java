package boj_23_0316;

import java.util.Scanner;

public class B_10952_덧셈 {

	private static int a, b;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		while (true) {
			a = sc.nextInt();
			b = sc.nextInt();
			if (a == 0 && b == 0) break;
			System.out.println(a+b);
		}

	}

}
