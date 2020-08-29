package BOJ;
/*
 * BOJ 1865
 * 벨만포드 알고리즘. 타임머신과 달리 웜홀이 포함될 때의 사이클 여부를 체크해야 함.
 */

import java.io.*;
import java.util.*;

public class WormHole {
	
	private static final long INF = Long.MAX_VALUE;

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		for(int tc = 0; tc < TC; tc++) {
			String[] info = br.readLine().split(" ");
			int n = Integer.parseInt(info[0]);
			int m = Integer.parseInt(info[1]);
			int w = Integer.parseInt(info[2]);
			
			List<Road> road = new ArrayList<Road>();
			
			for(int j = 0; j < m; j++) { //M road
				String[] set = br.readLine().split(" ");
				int s = Integer.parseInt(set[0]);
				int e = Integer.parseInt(set[1]);
				int t = Integer.parseInt(set[2]);
				road.add(new Road(s, e, t));
				road.add(new Road(e, s, t));
			}
			HashSet<Integer> hs = new HashSet<>();
			for(int k = 0; k < w; k++) { //W wormhole
				String[] set2 = br.readLine().split(" ");
				int s = Integer.parseInt(set2[0]);
				int e = Integer.parseInt(set2[1]);
				int t = Integer.parseInt(set2[2]);
				hs.add(s);
				road.add(new Road(s, e, -t));
			}
			
			boolean isCycle = false;
			long[] dist = new long[n+1];
			Arrays.fill(dist, INF);
			
			Iterator it = hs.iterator();
			
			while(it.hasNext()) {
				dist[(int)it.next()] = 0;
				
				for(int i = 1; i <= n; i++) {
					for(int j = 0; j < road.size(); j++) {
						int start = road.get(j).start;
						int end = road.get(j).end;
						int time = road.get(j).time;
						
						if(dist[start] != INF && dist[end] > dist[start]+time) {
							dist[end] = dist[start]+time;
							if(i == n)
								isCycle = true;
						}
					}
				}
				
				if(isCycle)
					break;
			}
			
			
			if(isCycle) {
				System.out.println("YES");
			}
			else
				System.out.println("NO");
			
		}

	}

}

class Road{
	int start, end, time;
	public Road(int start, int end, int time) {
		this.start = start;
		this.end = end;
		this.time = time;
	}
}
