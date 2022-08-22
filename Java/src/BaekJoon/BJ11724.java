package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class BJ11724 {
    static int[][] board;
    static boolean[] visited;
    static int N;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        int M = sc.nextInt();
        board = new int[N][N];
        visited = new boolean[N];
        int result = 0;

        for (int i = 0; i < M; i++) {
                int R = sc.nextInt() - 1;
                int C = sc.nextInt() - 1;
                board[R][C] = 1;
                board[C][R] = 1;
        }
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                dfs(i);
                result++;
            }
        }

        System.out.println(result);
    }

    public static void dfs(int row) {
        //System.out.println(row);
        visited[row] = true;
        for (int i = 0; i < N; i++) {
            if (!visited[i] && board[row][i] == 1) {
                dfs(i);
            }
        }
    }
}
