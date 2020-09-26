package BOJ;

import java.io.*;
import java.util.*;

/*
 * BOJ 2839
 * DP
 */

public class SugarDelivery {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int answer = 0;
		
		while(true) {
			if(N % 5 == 0) {
				answer += N/5;
				break;
			}
			else if(N < 0){
				answer = -1;
				break;
			}
			
			N -= 3;
			answer++;
			
		}
		System.out.println(answer);

	}

}
