package Programmers;

import java.util.HashMap;

/*
 * 참고 블로그 : https://jhnyang.tistory.com/120
 * HashMap
 */

public class Marathon {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

//		String[] participant = {"leo", "kiki", "eden"};
//		String[] completion = {"eden", "kiki"};
		
		String[] participant = {"marina", "josipa", "nikola", "vinko", "filipa"};
		String[] completion = {"josipa", "nikola", "vinko", "filipa"};
		
		solution(participant, completion);
		
		
	}
	public static String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> hm = new HashMap<>();
        for(int i = 0; i < participant.length; i++) {
        	hm.put(participant[i], hm.getOrDefault(participant[i], 0) +1);
        }
        for(int i = 0; i < completion.length; i++) {
        	hm.put(completion[i], hm.get(completion[i])-1);
        }
        for(String p : hm.keySet()) {
        	if(hm.get(p) != 0) {
        		answer = p;
        		break;
        	}
        }
        System.out.println(answer);
        
        return answer;
    }

}
