package boj_23_0327;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class B_2751_수정렬하기2 {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer>arr = new ArrayList<>();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		
		int N = sc.nextInt();
		
		for (int i = 0; i < N; i++) {
			arr.add(sc.nextInt());
		}
		Collections.sort(arr);
		for (int a : arr) {
			bw.write(Integer.toString(a));
			bw.write("\n");
		}
		bw.flush();
		
	}

}
