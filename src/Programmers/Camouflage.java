package Programmers;

/*
 * HighScoreKit - Hash
 * Lv 2.
 */

import java.util.*;

public class Camouflage {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		String[][] clothes = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
//		String[][] clothes = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
		String[][] clothes = {{"round_glasses", "face"}, {"black_sunglasses", "face"}, {"blue_tshirts", "top"}, {"jeans", "bottom"}, {"long_coat", "outer"}};
		
		solution(clothes);

	}
	
	public static int solution(String[][] clothes) {
		HashMap<String, Integer> hm = new HashMap<>();
        int answer = 0;
        
        for(int i = 0; i < clothes.length; i++) {
        	if(hm.containsKey(clothes[i][1])) {
        		hm.replace(clothes[i][1], hm.get(clothes[i][1])+1);
        	}
        	else {
            	hm.put(clothes[i][1], 1);
        	}
        }
        //낱개 하나씩 무조건 들어가고,같은 묶음인 것들 개수 끼리 곱하기
        
        int temp = 1;
        
        for(HashMap.Entry<String, Integer> it : hm.entrySet()) {
        	int val = it.getValue()+1;
        	temp *= val;
		}
        
        answer = temp - 1;
        
        System.out.println(answer);
        
        return answer;
    }

}
