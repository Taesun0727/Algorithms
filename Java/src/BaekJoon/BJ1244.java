package BaekJoon;

import java.util.Scanner;

public class BJ1244 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		int switch_Count = sc.nextInt();
		int[] switch_Status = new int[switch_Count];

		for (int i = 0; i < switch_Count; i++) {
			switch_Status[i] = sc.nextInt();
		}

		int student_Count = sc.nextInt();

		for (int i = 0; i < student_Count; i++) {
			int student_Sex = sc.nextInt();
			int student_Get_SwitchNumber = sc.nextInt() - 1;

			if (student_Sex == 1) { // 성별이 남자일 경우
				for (int j = student_Get_SwitchNumber; j < switch_Count; j += (student_Get_SwitchNumber + 1)) {
						switch_Status[j] = (switch_Status[j] == 1) ? 0 : 1;
				}

			} else if (student_Sex == 2) { // 성별이 여자일 경우
				switch_Status[student_Get_SwitchNumber] = (switch_Status[student_Get_SwitchNumber] == 1) ? 0 : 1;

				for (int j = 1; j < switch_Count / 2 + 1; j++) {
					if (student_Get_SwitchNumber - j >= 0 && student_Get_SwitchNumber + j < switch_Count) {
						if (switch_Status[student_Get_SwitchNumber - j] == switch_Status[student_Get_SwitchNumber + j]) {
							switch_Status[student_Get_SwitchNumber - j] = (switch_Status[student_Get_SwitchNumber - j] == 0) ? 1 : 0;
							switch_Status[student_Get_SwitchNumber + j] = (switch_Status[student_Get_SwitchNumber + j] == 0) ? 1 : 0;
						} else {
							break;
						}
					} else {
						break;
					}
				}

			}
		}

		for (int i = 0; i < switch_Count; i++) {
			System.out.print(switch_Status[i] + " ");
			if ((i+1) % 20 == 0) {
				System.out.println();
			}
		}
	}
}
