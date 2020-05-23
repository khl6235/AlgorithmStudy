package week2;

/*
 * programmers level 2 - Tuple
 */

import java.util.ArrayList;
import java.util.Comparator;

public class Tuple {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		String s = "{{2},{2,1},{2,1,3},{2,1,3,4}}";
		String s = "{{1,2,3},{2,1},{1,2,4,3},{2}}";
//		String s = "{{4,2,3},{3},{2,3,4,1},{2,3}}";
//		String s = "{{20,111},{111}}";
		
		solution(s);

	}
	

    public static int[] solution(String s) {
    	ArrayList<String> sub = new ArrayList<String>();
    	ArrayList<Integer> sub2 = new ArrayList<Integer>();
        int[] answer;
        int start = 0;
        int end = 0;
        
        for(int i = 1; i < s.length()-1; i++) {
        	if(s.charAt(i) == '{') {
        		start = i+1;
        	}
        	if(s.charAt(i) == '}') {
        		end = i;
        		sub.add(s.substring(start, end));
        	}
        }
        
        //sort the ArrayList by element length
        sub.sort(new Comparator<String>() {
        	@Override
        	public int compare(String o1, String o2) {
        		if(o1.length() == o2.length()) {
        			return o1.compareTo(o2);
        		}
        		else {
        			return Integer.compare(o1.length(), o2.length());
        		}
        	}
        });
        
        answer = new int[sub.size()];
        
        for(int i = 0; i < sub.size(); i++) {
        	System.out.println("["+i+"] "+sub.get(i));
        	if(i == 0) {
        		answer[0] = Integer.parseInt(sub.get(i));
        	}
        	else { //i>1
        		int start2 = 0;
        		int end2 = 0;
        		for(int j = 0; j < sub.get(i).length(); j++) {
        			if(sub.get(i).charAt(j) == ',') {
        				end2 = j;
        				sub2.add(Integer.parseInt(sub.get(i).substring(start2,end2)));
        				start2 = j+1;
        			}
        			else if(j == sub.get(i).length()-1) {
        				sub2.add(Integer.parseInt(sub.get(i).substring(start2)));
        			}
        		}
        		
        		System.out.println(sub2);
        		for(int j = 0; j < sub2.size(); j++) {
        			int tmp = sub2.get(j);
        			
        			boolean flag = false;
        			for(int k = 0; k < i; k++) {
        				if(answer[k] == tmp) {
        					System.out.println("pass");
        					flag = true;
        					break;
        				}
        			}
        			if(!flag) {
        				answer[i] = tmp;
        				System.out.println(answer[i]);
        			}
        			
        		}
        	}
        }
         
        
        return answer;
    }

}
