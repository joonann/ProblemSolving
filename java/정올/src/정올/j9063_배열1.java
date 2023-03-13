package 정올;
import java.util.Scanner;

public class j9063_배열1 { //제출 시 클래스명을 Main으로 수정

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] a = new int[5];
		
		for (int i = 0; i < 5; i++) {
			a[i] = sc.nextInt();
		}
		// 출력
		for (int i = 0; i < 5; i++) {
			System.out.print(a[i]+" ");
		}
	}

}
