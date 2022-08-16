package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ2669 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] board = new int[101][101];
		int result = 0;
		
		for (int i = 0; i < 4; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int start_y = Integer.parseInt(st.nextToken());
			int start_x = Integer.parseInt(st.nextToken());
			int end_y = Integer.parseInt(st.nextToken());
			int end_x = Integer.parseInt(st.nextToken());
			
			for (int j = start_x; j < end_x; j++) {
				for (int k = start_y; k < end_y; k++) {
					board[j][k] = 1;
				}
			}
			
		}
		
		for (int j = 0; j < 101; j++) {
			for (int k = 0; k < 101; k++) {
				if (board[j][k] == 1) {
					result++;
				}
			}
		}
		System.out.println(result);
		

	}

}
