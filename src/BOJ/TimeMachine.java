package BOJ;

/*
 * BOJ 11657
 * 벨만포드 알고리즘. Dijkstra와 달리 음수 가중치, 사이클 검사 가능.
 */

import java.io.*;
import java.util.*;

public class TimeMachine {

	private static final long INF = Long.MAX_VALUE;

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int N = Integer.parseInt(str[0]);
		int M = Integer.parseInt(str[1]);
		
		List<Bus> bus = new ArrayList<Bus>();
		for(int m = 0; m < M; m++) {
			String[] str2 = br.readLine().split(" ");
			int A = Integer.parseInt(str2[0]);
			int B = Integer.parseInt(str2[1]);
			int C = Integer.parseInt(str2[2]);
			bus.add(new Bus(A, B, C)); //Bus list info
		}

		long[] dist = new long[N+1];
		Arrays.fill(dist, INF); //initiate dist[]
		
		dist[1] = 0;
		boolean isCycle = false;
		
		for(int i = 1; i <= N; i++) { // not i < N, i <= N. -> minimum dist one more check(if there's loop, minimum dist linearly decrease
			for(int j = 0; j < M; j++) { //every Bus courses
				int start = bus.get(j).start;
				int end = bus.get(j).end;
				int time = bus.get(j).time;
				
				if(dist[start] != INF && dist[end] > dist[start]+time) { //check every dist
					dist[end] = dist[start]+time;
					if(i == N) {
						isCycle = true;
					}
				}
			}
		}
		
		
		if(isCycle) {
			System.out.println(-1);
		}
		else {
			for(int i = 2; i <= N; i++) {
				System.out.println(dist[i] == INF ? -1 : dist[i]);
			}
		}
		
	}

}

class Bus{
	int start, end, time;
	public Bus(int start, int end, int time) {
		this.start = start;
		this.end = end;
		this.time = time;
	}
}
