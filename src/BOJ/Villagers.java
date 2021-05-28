package BOJ;

/*
BOJ #2644
[BFS]
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Graph{
	private int V;
	private int adj[][];
	
	Graph(int v){
		V = v;
		adj = new int[v][v];
		for(int i = 0; i < v; i++)
			for(int j = 0; j < v; j++)
				adj[i][j] = 0;
		
	}
	
	void addEdge(int v, int w) {
		adj[v][w] = 1;
		adj[w][v] = 1;
	}
	
	int BFS(int s_node, int e_node) {
		LinkedList<Integer> queue = new LinkedList<Integer>();
		int dist[] = new int[V];
		int n = 0;
		
		queue.add(s_node);
		
		while(queue.size()!= 0) {
			int tmp = queue.remove();
			for(int i = 0; i < V; i++) {
				if(adj[tmp][i] == 0 || dist[i] != 0)
					continue;
				dist[i] = dist[tmp]+1;
				if(i == e_node)
					break;
				queue.add(i);
			}	
		}
		
		if(dist[e_node] == 0) return -1;
		return dist[e_node];
	}
}

public class Villagers {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		Graph g = new Graph(n+1);
		
		String[] str = br.readLine().split(" ");
		int p1 = Integer.parseInt(str[0]);
		int p2 = Integer.parseInt(str[1]);
		
		int m = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < m; i++) {
			StringTokenizer init = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(init.nextToken());
			int y = Integer.parseInt(init.nextToken());
			g.addEdge(x, y);
		}
		
		System.out.println(g.BFS(p1, p2));
		
	}

}
