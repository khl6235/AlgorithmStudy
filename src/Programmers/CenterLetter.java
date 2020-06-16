package Programmers;

public class CenterLetter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		String s = "abcde";
		String s = "qwer";
		
		solution(s);

	}
	
	public static String solution(String s) {
        String answer = "";
        
        if(s.length()%2 == 1) {
        	answer = s.substring(s.length()/2, s.length()/2+1);
        }
        else {
        	answer = s.substring(s.length()/2-1, s.length()/2+1);
        }
        
        System.out.println(answer);
        
        return answer;
    }

}
