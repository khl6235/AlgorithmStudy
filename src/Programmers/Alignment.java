package Programmers;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

/*
 * programmers K번째 
 */

public class Alignment {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] array = {1, 5, 2, 6, 3, 7, 4};
		int[][] commands = {
				{2,5,3},
				{4,4,1},
				{1,7,3}
		};
		
		solution(array, commands);
		

	}
	
	public static int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < array.length; i++) {
        	list.add(array[i]);
        }
        
        for(int i = 0; i < commands.length; i++) {
        	int first = commands[i][0]-1;
        	int last = commands[i][1];
        	if(last == array.length) {
        		List<Integer> newarr = new ArrayList<>(list.subList(first, last));
        		newarr.add(array[array.length-1]);
        	}
        	List<Integer> newarr = new ArrayList<>(list.subList(first, last));
//        	array.subList(commands[i][0]-1, commands[i][1])
//        	System.out.println(newarr);
        	Collections.sort(newarr);
//        	System.out.println(newarr);
        	answer[i] = newarr.get(commands[i][2]-1);
        }
        
        for(int i = 0; i < answer.length; i++) {
        	System.out.println(answer[i]);
        }
        
        return answer;
    }

}
