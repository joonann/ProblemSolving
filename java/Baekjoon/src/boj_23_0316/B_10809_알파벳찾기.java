package boj_23_0316;

import java.util.Scanner;

public class B_10809_알파벳찾기 {

	private static int[] arrOutput = new int[26];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s1 = sc.next();
		char[] arrInput = s1.toCharArray();
		
		for (int i = 0; i < 26; i++) 
			arrOutput[i]= -1;
		
		for (int i = 0; i < arrInput.length; i++) {
			int a = (char)arrInput[i] - 'a';
			if (arrOutput[a] == -1)
				arrOutput[a] = i;
		}
		for (int i = 0; i < arrOutput.length; i++) {
			System.out.print(arrOutput[i]+" ");
		}
		
	}

}
