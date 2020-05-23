package Programmers;

/*
 * programmers level 1 - Crane Picking Game
 */

import java.util.ArrayList;

public class CraneGame {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[][] board = {
				{0,0,0,0,0},
				{0,0,1,0,3},
				{0,2,5,0,1},
				{4,2,4,4,2},
				{3,5,1,3,1}};
		
		int[] moves = {1,5,3,5,1,2,1,4};
		
		solution(board, moves);

	}
	
	public static int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Integer> bucket = new ArrayList<Integer>();
        
        for(int i = 0; i < moves.length; i++) {
        	int line = moves[i]-1;
        	for(int j = 0; j < board.length; j++) {
        		if(board[j][line] != 0) {
        			bucket.add(board[j][line]); 
        			board[j][line] = 0;
        			break;
        		}
        	}
        	
        	if(bucket.size() >=2 && bucket.get(bucket.size()-1) == bucket.get(bucket.size()-2)) {
        		bucket.remove(bucket.size()-1);
        		bucket.remove(bucket.size()-1);
        		answer += 2;
        	}
        	
        }
        System.out.println(answer);
        
        return answer;
    }

}
