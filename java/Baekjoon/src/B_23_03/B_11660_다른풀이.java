package B_23_03;

import java.util.Scanner;

public class B_11660_다른풀이 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int arr[] = new int[N];
        int Max = -1000001, Min = 1000001;
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
            if (arr[i] < Min) Min = arr[i];
            if (arr[i] > Max) Max = arr[i];
        }
        System.out.println(Min+" "+Max);
    }
}