package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BJ2670 {
	
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		double max = 0;
		double[] arr = new double[N];
		
		for (int i = 0; i < N; i++) {
			double tmp = Double.parseDouble(br.readLine());
			arr[i] = tmp;
			if (max < tmp) {
				max = tmp;
			}
		}
		
		for (int i = 0; i < N; i++) {
			double current_value = arr[i];
			for (int j = i+1; j < N; j++) {
				current_value *= arr[j];
				if (max < current_value) {
					max = current_value;
				}
			}
		}
		
		System.out.printf("%.3f", max);
		
	}
	

}
