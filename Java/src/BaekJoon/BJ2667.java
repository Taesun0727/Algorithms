package BaekJoon;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class BJ2667 {
	
	static int N, Ap_complex;
	static char[][] board;
	static int[][] delta = { {1, 0}, {0, 1}, {-1, 0}, {0, -1} };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		board = new char[N][N];
		ArrayList<Integer> result = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			board[i] = br.readLine().toCharArray();
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] == '1') {
					Ap_complex = 0;
					Dfs(i, j);
					result.add(Ap_complex);
				}
			}
		}
		
		Collections.sort(result);
		
		// 정답출력
		System.out.println(result.size());
		for (int i = 0; i < result.size(); i++) {
			System.out.println(result.get(i));
		}
	}
	
	public static void Dfs(int x, int y) {
		board[x][y] = '0';
		Ap_complex++;
		
		for (int i = 0; i < 4; i++) {
			int next_x = x + delta[i][0];
			int next_y = y + delta[i][1];
			
			if (next_x >= 0 && next_x < N && next_y >= 0 && next_y < N && board[next_x][next_y] == '1') {
				Dfs(next_x, next_y);
			}
		}
	}

}
