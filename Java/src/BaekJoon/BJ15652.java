package BaekJoon;

import java.util.Scanner;

public class BJ15652 {
	
	static int N;
	static int M;
	static int[] arr, num;
	static StringBuilder sb;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N];
		num = new int[M];
		for (int i = 1; i <=N; i++) {
			arr[i-1] = i;
		}
		sb = new StringBuilder();
		comb(0, 0);
		System.out.println(sb);
		
	}
	private static void comb(int cnt, int start) {
		if (cnt == M) {
			for (int i = 0; i < cnt; i++) {
				sb.append(num[i] + " ");
			}
			sb.append("\n");
			return;
		}
		for (int i = 0; i < N; i++) {
			num[cnt] = arr[i];
			comb(cnt+1, i + 1);
		}
	}

}
