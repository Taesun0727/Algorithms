package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ4963 {
    static int R;
    static int C;
    static int[][] board;
    static int[][] delta = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            C = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            int result = 0;
            if (C == 0 && R == 0) {
                break;
            }
            board = new int[R][C];
            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (board[i][j] == 1) {
                        dfs(i, j);
                        result++;
                    }
                }
            }
            System.out.println(result);
        }
    }
    public static void dfs(int x, int y) {
        board[x][y] = 0;

        for (int i = 0; i < 8; i++) {
            int nx = x + delta[i][0];
            int ny = y + delta[i][1];
            if (nx >= 0 && ny >= 0 && nx < R && ny < C && board[nx][ny] == 1) {
                dfs(nx, ny);
            }
        }
    }
}
