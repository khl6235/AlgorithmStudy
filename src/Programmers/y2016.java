package Programmers;

public class y2016 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int a = 5;
		int b = 24;
		solution(a, b);
		
		//Jan 1st = Friday

	}

	public static String solution(int a, int b) {
        String answer = "";
        
        int[] month = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int days = 0;
        
        for(int i  = 0; i < a-1; i++) {
        	days += month[i];
        }
        
        days += b;
        int result = days % 7;
        switch(result) {
        case 0 :
        	answer = "THU";
        	break;
        case 1 :
        	answer = "FRI";
        	break;
        case 2 :
        	answer = "SAT";
        	break;
        case 3 :
        	answer = "SUN";
        	break;
        case 4 :
        	answer = "MON";
        	break;
        case 5 :
        	answer = "TUE";
        	break;
        case 6 :
        	answer = "WED";
        	break;
        default :
        	break;
        
        }
        System.out.println(answer);
        
        return answer;
    }
}
