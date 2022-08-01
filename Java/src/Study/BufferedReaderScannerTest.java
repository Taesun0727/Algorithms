package Study;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class BufferedReaderScannerTest {

//	public static void main(String[] args) throws FileNotFoundException {
//		// TODO Auto-generated method stub
//		System.setIn(new FileInputStream("inputTC.txt"));
//		Scanner sc = new Scanner(System.in);
//
//		int Tc = sc.nextInt();
//		for (int tc = 1; tc <= Tc; tc++) {
//			int N = sc.nextInt();
//			
//			int sum = 0;
//			for (int i = 0; i < N; i++) {
//				for (int j = 0; j < N; j++) {
//					sum += sc.nextInt();
//				}
//			}
//			System.out.println("#" + tc + " " + sum);
//		}
//	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		//System.setIn(new FileInputStream("/Macintosh HD/Users/Documents/Algorithms/java/src/study/inputTC.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int Tc = Integer.parseInt(in.readLine());
		for (int tc = 1; tc <= Tc; tc++) {
			int N = Integer.parseInt(in.readLine());
			
			int sum = 0;
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(in.readLine(), " ");
				for (int j = 0; j < N; j++) {
					sum += Integer.parseInt(st.nextToken());
				}
			}
			System.out.println("#" + tc + " " + sum);
		}
	}

}
