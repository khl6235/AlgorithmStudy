package week1;

/*
 BOJ - 3109
 [DFS]
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Bakery {

	static int[] d = {-1, 0, 1};
	static int R;
	static int C;
	static boolean[][] arr;
	static int number;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer init = new StringTokenizer(br.readLine(), " ");
		
		R = Integer.parseInt(init.nextToken());
		C = Integer.parseInt(init.nextToken());
		arr = new boolean[R][C];
		
		number = 0;
		
		for(int i = 0; i < R; i++) {
			String row = br.readLine();
			for(int j = 0; j < C; j++) {
				if(row.charAt(j)=='x')
					arr[i][j] = true;
			}
		}
		
		
		for(int i = 0; i < R; i++) {
			if(Pipe(i, 0)) {
				number++;
			}
		}
		System.out.println("result : "+number);

	}
	
	public static boolean Pipe(int r, int c) {
		System.out.println("r: "+r+" c: "+c);
		
		
		for(int j = 0; j < 3; j++) {
			int nextR = r + d[j];
			int nextC = c + 1;
			
			if(nextC == C-1)
				return true;
				
			if(nextR >= 0 && nextC >= 0 && nextR < R && nextC < C && arr[nextR][nextC] == false) {
				arr[nextR][nextC] = true;
				System.out.println(nextR+" "+nextC);
				if(Pipe(nextR, nextC)) {
					return true;
				}
				
			}
				
		}

		return false;

	}
	
}
