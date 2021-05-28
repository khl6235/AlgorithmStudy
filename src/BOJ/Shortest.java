package BOJ;

/*
BOJ #1753
[Dijkstra] (PriorityQueue 써야함, ArrayList<List<Node>>() 인접리스트 사 -> 메모리초과, 시간초과...)
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

//class Edge{
//	int end;
//	int val;
//	
//	Edge(int end, int val){
//		this.end = end;
//		this.val = val;
//	}
//}

public class Shortest {
	static int V, E;
	static int dist[];
	static List<List<Node>> list;
	
	static class Node implements Comparable<Node> {
        int index, distance;
 
        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }
 
        public int compareTo(Node n) {
            return this.distance - n.distance;
        }
    }
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] str = br.readLine().split(" ");
		int V = Integer.parseInt(str[0]);
		int E = Integer.parseInt(str[1]);
		int k = Integer.parseInt(br.readLine());
		
		dist = new int[V+1];
		list = new ArrayList<List<Node>>();
		
		Arrays.fill(dist, Integer.MAX_VALUE);
		
//		ArrayList<Edge>[] edge = new ArrayList[V+1];
		
		list.add(new ArrayList<Node>());
		for(int i = 1; i <= V; i++)
			list.add(new ArrayList<Node>());
//			edge[i] = new ArrayList<Edge>();
		
		for(int i = 0; i < E; i++) {
			String[] str2 = br.readLine().split(" ");
			int u = Integer.parseInt(str2[0]);
			int v = Integer.parseInt(str2[1]);
			int w = Integer.parseInt(str2[2]);
//			edge[u].add(new Edge(v, w));
			list.get(u).add(new Node(v, w));
		}
		
		boolean[] visited = new boolean[V+1];
		PriorityQueue<Node> pq = new PriorityQueue<Node>();
		pq.add(new Node(k, 0));
		dist[k] = 0;
		
		while(!pq.isEmpty()) {
			int now = pq.poll().index;

			if(visited[now]) continue;
			visited[now] = true;
			
//			for(int i = 0; i < edge[now].size(); i++) {
//				int next = edge[now].get(i).end; //다음 vertex
//				int value = edge[now].get(i).val; //그 사이 weight
//				
//				if(dist[next] > dist[now]+value) {
//					dist[next] = dist[now]+value;
//					pq.add(next);
//				}
//			}
			for(Node node : list.get(now)) {
                if(dist[node.index] > dist[now] + node.distance) {
                    dist[node.index] = dist[now] + node.distance;
                    pq.add(new Node(node.index, dist[node.index]));
                }
            }
		}

		for(int i = 1; i <= V; i++) {
			if(dist[i] == Integer.MAX_VALUE)
				bw.write("INF\n");
			else
				bw.write(dist[i] + "\n");
		}
		bw.flush();
        bw.close();

	}

}
