package Programmers;

/*
 * programmers level 1 - MockExam
 * 참고 : https://sas-study.tistory.com/240
 */

import java.util.ArrayList;

public class MockExam {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		int[] answers = {1,2,3,4,5};
		int[] answers = {1,3,2,4,2};
		solution(answers);

	}
	
	public static int[] solution(int[] answers) {
        int[] answer;
        
        int[] p1 = {1,2,3,4,5};
        int[] p2 = {2,1,2,3,2,4,2,5};
        int[] p3 = {3,3,1,1,2,2,4,4,5,5};
        
        int r1 = 0;
        int r2 = 0;
        int r3 = 0;
        
        for(int i = 0; i < answers.length; i++) {
        	if(p1[i%p1.length] == answers[i])
        		r1++;
        	if(p2[i%p2.length] == answers[i])
        		r2++;
        	if(p3[i%p3.length] == answers[i])
        		r3++;
        	
        }
        
        ArrayList<Integer> ans = new ArrayList<Integer>();
        int max = Math.max(Math.max(r1, r2), r3);
        
        if(max == r1)
        	ans.add(1);
        if(max == r2)
        	ans.add(2);
        if(max == r3)
        	ans.add(3);
        
        answer = new int[ans.size()];
        
        for(int i = 0; i < ans.size(); i++)
        	answer[i] = ans.get(i);
        	
        
        for(int i = 0; i < answer.length; i++)
        	System.out.println(answer[i]);
        
        return answer;
    }

}
