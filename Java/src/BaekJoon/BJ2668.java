package BaekJoon;

import java.util.*;

public class BJ2668 {
	
	static int[] arr;
	static boolean[] visited;
	static ArrayList<Integer> result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		arr = new int[N+1];
		arr[0] = 0;
		visited = new boolean[N+1];
		result = new ArrayList<>();
		
		for (int i = 1; i <= N; i++) {
			arr[i] = sc.nextInt();
		}
		
		for (int i = 1; i <= N; i++) {
			visited[i] = true;
			DFS(i, i);
			visited[i] = false;
		}
		
		Collections.sort(result);
		
		// 결과출력
		System.out.println(result.size());
		for (int i = 0; i < result.size(); i++) {
			System.out.println(result.get(i));
		}

	}
	
	public static void DFS(int i, int target) {
		if (visited[arr[i]] == false) {
			visited[arr[i]] = true;
			DFS(arr[i], target);
			visited[arr[i]] = false;
		}
		
		if (target == arr[i]) {
			result.add(target);
		}
	}

}
