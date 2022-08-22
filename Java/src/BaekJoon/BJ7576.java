package BaekJoon;

import java.util.*;
import java.io.*;
import java.awt.Point;

public class BJ7576 {

    static int[][] delta = {{ -1, 0 }, {0, 1}, {1, 0}, {0, -1}};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int C = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int[][] board = new int[R][C];
        int[][] check_board = new int[R][C];
        boolean check = true;
        Queue<Point> queue = new LinkedList<>();

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                board[i][j] = tmp;
                if (tmp == 1) {
                    Point p = new Point(i,j);
                    queue.offer(p);
                } else if(tmp == 0) {
                    check = false;
                }
            }
        }
        //System.out.println(Arrays.deepToString(board));
        if (check) {
            System.out.println(0);
        } else {
            while (!queue.isEmpty()) {
                Point tmp = queue.poll();
                for (int i = 0; i < 4; i++) {
                    int n_x = tmp.x + delta[i][0];
                    int n_y = tmp.y + delta[i][1];
                    if(n_x >= 0 && n_y >= 0 && n_x < R && n_y < C && board[n_x][n_y] == 0) {
                        check_board[n_x][n_y] = check_board[tmp.x][tmp.y] + 1;
                        board[n_x][n_y] = 1;
                        queue.offer(new Point(n_x, n_y));
                    }
                }
            }
            int result = 0;
            check = true;
            //System.out.println(Arrays.deepToString(board));
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (board[i][j] == 0) {
                        check = false;
                    }
                    result = Math.max(result, check_board[i][j]);
                }
            }
            if (!check) {
                System.out.println(-1);
            } else {
                System.out.println(result);
            }
        }



    }
}
