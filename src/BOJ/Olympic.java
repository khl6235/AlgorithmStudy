package BOJ;

/*
BOJ #8979
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Olympic {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int N = Integer.parseInt(str[0]);
		int K = Integer.parseInt(str[1]);
		
		int[][] medal = new int[1000][4];
		int here = 0;
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			medal[i][0] = Integer.parseInt(st.nextToken()); //country
			if(medal[i][0] == K) {
				here = i;
			}
			medal[i][1] = Integer.parseInt(st.nextToken()); //gold
			medal[i][2] = Integer.parseInt(st.nextToken()); //silver
			medal[i][3] = Integer.parseInt(st.nextToken()); //bronze
			
		}
		
		int gold = medal[here][1];
		int silver = medal[here][2];
		int bronze = medal[here][3];

		int count = 0;
		
		for(int i = 0; i < N; i++) {
			if(i == here) continue;
			if(gold < medal[i][1]) {
				count++;
				continue;
			}
			else if(gold == medal[i][1]) {
				if(silver < medal[i][2]) {
					count++;
					continue;
				}
				else if(silver == medal[i][2]) {
					if(bronze < medal[i][3]) {
						count++;
						continue;
					}
				}
			}
			
		}
		System.out.println(count+1);
		


	}

}
