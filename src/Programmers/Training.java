package Programmers;

/*
 * 참고 블로그 : https://moonong.tistory.com/17
 * Java Greedy
 */

public class Training {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int n = 5;
		int[] lost = {2, 4};
		int[] reserve = {1, 3, 5};
		
		solution(n, lost, reserve);
		
	}

	public static int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        
      //여벌 있는 사람이 잃어버렸으면 자기몫만 챙겨야 되므로 answer++하고 값 변경 
        for(int i = 0; i < reserve.length; i++) {
        	for(int j = 0; j < lost.length; j++) {
        		if(reserve[i] == lost[j]) {
        			reserve[i] = 0;
        			answer++;
        			lost[j] = 0;
        			break;
        		}
        	}
        }
        
        //잃어버린사람, 여벌 있는 사람 간격이 1이면 빌려주기 
        for(int i = 0; i < reserve.length; i++) {
        	for(int j = 0; j < lost.length; j++) {
        		if(reserve[i] != 0 && lost[j] != 0) {
        			if(Math.abs(reserve[i] - lost[j]) == 1) {
        				reserve[i] = 0;
        				answer++;
        				lost[j] = 0;
        				break;
        			}
        		}
        	}
        }
        System.out.println(answer);
        
        return answer;
    }
}
