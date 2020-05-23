package week1;

/*
BOJ #4485
[Dijkstra] (DP+DFS -> 실패)
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Zelda {
	
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int count = 0;
		
		while(true) {
			int n = Integer.parseInt(br.readLine());
			if(n == 0) break;
			
			int cave[][] = new int[n][n];
			boolean visited[][] = new boolean[n][n];
			int dist[][] = new int[n][n];
			count++;
			
			for(int i = 0; i < n; i++) {
				StringTokenizer init = new StringTokenizer(br.readLine(), " ");
				for(int j = 0; j < n; j++) {
					cave[i][j] = Integer.parseInt(init.nextToken());
					dist[i][j] = Integer.MAX_VALUE;
				}
			}
			
			System.out.println("Problem "+count+": "+Moving(new Node(0,0,cave[0][0]), cave, dist, n));
			
		}

	}
	
	static int Moving(Node node, int cave[][], int dist[][], int n) {
		
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(node);
		
		dist[node.x][node.y] = cave[node.x][node.y];
		
		while(!pq.isEmpty()) {
			Node now = pq.poll();
			if(dist[now.x][now.y] < now.rupee)
				continue;
			for(int k = 0; k < 4; k++) {
				int nextX = now.x + dx[k];
				int nextY = now.y + dy[k];
				
				if(nextX < 0 || nextY < 0 || nextX >= n || nextY >= n)
					continue;
				
				if(dist[nextX][nextY] > dist[now.x][now.y] + cave[nextX][nextY]) {
					dist[nextX][nextY] = dist[now.x][now.y] + cave[nextX][nextY];
					pq.add(new Node(nextX, nextY, dist[nextX][nextY]));
				}
				
			}
		}
		
		return dist[n-1][n-1];
		
		
//		int nowX = 0;
//		int nowY = 0;
//		int sum = cave[nowX][nowY];
//		
////		System.out.println(sum);
//		
//		while(nowX+nowY < 2*(n-1)) {//한칸 전진	
//			int less = 10;
//			int nextX = 0;
//			int nextY = 0;
//			
//			for(int k = 0; k < 4; k++) {
//				int nX = nowX + dx[k];
//				int nY = nowY + dy[k];
//				
//				if(nX < 0 || nY < 0 || nX >= n || nY >= n || visited[nX][nY])
//					continue;
//				
//				if(nX == nowX-1 || nY == nowY-1) {
//					
//				}
//				int temp = cave[nX][nY];
//				if(temp < less) {
//					less = temp;
//					nextX = nX;
//					nextY = nY;
//					System.out.println("nextX : "+ nextX + " nextY : "+nextY);
//				}
//			}
//			sum += less;
//			System.out.println(sum);
//			nowX = nextX;
//			nowY = nextY;
//			visited[nowX][nowY] = true;
//			System.out.println("nowX : "+ nowX + " nowY : "+nowY);
//			
//		}
//		//System.out.println(sum);
//		return sum;
	}

}

class Node implements Comparable<Node>{
	int x, y, rupee;
	
	Node(int x, int y, int rupee){
		this.x = x;
		this.y = y;
		this.rupee = rupee;
	}
	
	@Override
	public int compareTo(Node a) {
		if(this.rupee <= a.rupee)
			return -1;
		return 1;
	}
}
