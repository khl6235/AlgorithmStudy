package BOJ;

/*
 * [BOJ] 2003
 * Two pointers
 * ref : https://118k.tistory.com/702
 */

import java.io.*;
import java.util.*;

public class NumberHap2 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		int N = Integer.parseInt(str[0]);
		int M = Integer.parseInt(str[1]);
		int[] A = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}

		int count = 0;
		int sum = 0;
		int end = 0;
		
		for(int start = 0; start < N; start++) {
			sum += A[start];
			
			if(sum == M) {
				sum -= A[end];
				end++;
				count++;
			}
			else if(sum > M) {
				while(sum > M) {
					sum -= A[end];
					end++;
					if(sum == M) {
						count++;
					}
				}
			}
		}
		
		System.out.println(count);
		
	}

}
