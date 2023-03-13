package boj_23_0313;

아직 못 풀었다
public class B_24090_퀵정렬1 {
	
	public static void swap(int[] A, int i, int j) {
		int temp = A[i];
		A[i] = A[j];
		A[j] = temp;
	}

	public static void quickSort(int[] A, int p, int r) {
	
	}

	public static int partition(int[] A, int p, int r) {
		int x = A[r];
		int i = p - 1;
		for (int j = p; j < r - 1; j++) {
			if (A[j] <= x) {
				swap(A, ++i, j);
			}
		}
		if (i + 1 != r) {
			swap(A, i + 1, r);
		}
		return i + 1;
	}

	public static void main(String[] args) {

	}

}
