package BaekJoon;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ2178 {
    static int[][] delta = {{-1, 0} , {0, 1}, {1, 0}, {0, -1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int[][] maze = new int[R][C];
        int[][] visited = new int[R][C];
        for (int i = 0; i < R; i++) {
            String s = br.readLine();
            for (int j = 0; j < C; j++) {
                maze[i][j] = s.charAt(j) - '0';
                visited[i][j] = Integer.MAX_VALUE;
            }
        }
        Queue<Point> queue = new LinkedList<>();
        visited[0][0] = 1;
        queue.offer(new Point(0, 0));



        while (!queue.isEmpty()) {
            Point tmp = queue.poll();
            for (int i = 0; i < 4; i++) {
                int n_x = tmp.x + delta[i][0];
                int n_y = tmp.y + delta[i][1];
                if (n_x >= 0 && n_y >= 0 && n_x < R && n_y < C && maze[n_x][n_y] == 1) {
                    if (visited[n_x][n_y] > visited[tmp.x][tmp.y] + 1) {
                        visited[n_x][n_y] = visited[tmp.x][tmp.y] + 1;
                        queue.offer(new Point(n_x, n_y));
                    }
                }
            }
        }
        //System.out.println(Arrays.deepToString(visited));
        System.out.println(visited[R-1][C-1]);
    }
}
