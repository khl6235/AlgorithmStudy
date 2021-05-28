package BOJ;

/*
BOJ #3052
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Modulo {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int arr[] = new int[10];
		for(int i = 0; i < 10; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			arr[i] = arr[i] % 42;
		}
		
		ArrayList<Integer> result = new ArrayList<Integer>();
		for(int i = 0; i < 10; i++) {
			result.add(arr[i]);
			for(int j = 0; j < result.size()-1; j++) {
				if(arr[i] == result.get(j)) {
					result.remove(j);
				}
			}

		}
		
		System.out.println(result.size());
		
	}

}
