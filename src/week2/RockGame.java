package week2;

import java.util.Scanner;

public class RockGame {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		
		if(N%2==0) {
			System.out.println("CY");
		}
		else {
			System.out.println("SK");
		}

	}

}
