package Programmers;

/*
 * HighScoreKit - Hash
 * Lv 2.
 */

import java.util.*;

public class PhoneNumList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String[] phone_book = {"119", "97674223", "1195524421"};
		
		solution(phone_book);

	}
	
	public static boolean solution(String[] phone_book) {
		HashMap<String, Integer> hm = new HashMap<>();
        boolean answer = true;
        
        for(int i = 0; i < phone_book.length; i++) {
        	for(int j = 1; j < phone_book[i].length(); j++) {
        		hm.put(phone_book[i].substring(0, j), 1);
        	}
        }
        
        for(int i = 0; i < phone_book.length; i++) {
        	if(hm.containsKey(phone_book[i])) {
        		answer = false;
        	}
        	else
        		hm.put(phone_book[i], 1);
        }
        
        return answer;
    }

}
