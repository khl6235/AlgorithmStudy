package BOJ;

/*
BOJ #2563
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Paper {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] paper = new int[100][100];
		int cnt = 0;
		
		int N = Integer.parseInt(br.readLine());
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			for(int j = a; j < a+10; j++) {
				for(int k = b; k < b+10; k++)
					paper[j][k] = 1;
			}	
		}
		
		
		for(int i = 0; i < 100; i++) {
			for(int j = 0; j < 100; j++) {
				if(paper[i][j] == 1)
					cnt++;
			}
		}
		
		System.out.println(cnt);

	}

}
