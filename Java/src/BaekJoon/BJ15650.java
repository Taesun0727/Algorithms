package BaekJoon;
import java.util.Scanner;

public class BJ15650 {
	static int N;
	static int M;
	static int[] arr, num;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N];
		num = new int[M];
		for (int i = 1; i <=N; i++) {
			arr[i-1] = i;
		}
		comb(0, 0);
		
	}
	private static void comb(int cnt, int start) {
		if (cnt == M) {
			for (int i = 0; i < cnt; i++) {
				System.out.print(num[i] + " ");
			}
			System.out.println();
			return;
		}
		for (int i = start; i < N; i++) {
			num[cnt] = arr[i];
			comb(cnt+1, i+1);
		}
	}

}
