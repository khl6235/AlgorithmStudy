package Programmers;

/*
 * HighScoreKit - Hash
 * Lv 1.
 */

import java.util.*;

public class Unreached {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] participant = {"leo", "kiki", "eden"};
		String[] completion = {"eden", "kiki"};
		
		System.out.println(solution(participant, completion));

	}

	public static String solution(String[] participant, String[] completion) {
		HashMap<String, Integer> hm = new HashMap<>();
		String answer = "";
		
		for(int i = 0; i < participant.length; i++) {
			if(hm.containsKey(participant[i])) {
				hm.replace(participant[i], hm.get(participant[i])+1);
			}
			else {
				hm.put(participant[i], 1);
			}
		}
		
		for(int i = 0; i < completion.length; i++) {
			if(hm.containsKey(completion[i])) {
				int num = hm.get(completion[i]);
				
				if(num == 1) {
					hm.remove(completion[i]);
				}
				else if(num > 1) {
					hm.replace(completion[i], num-1);
				}
				else
					answer = completion[i];
			}
		}
		
		// hashmap 출력 시, key-value 둘다 필요할 경우 entrySet(), key만 필요할 경우 keySet() or get(key)
		// keySet 시간 많이 걸려서 많은 양의 데이터 처리 시 entrySet()
		for(HashMap.Entry<String, Integer> it : hm.entrySet()) {
			if(it.getValue() > 0)
				return it.getKey();
		}
		
        return answer;
    }
	
}