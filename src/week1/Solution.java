/*
 * Google Women's I/O #1 problem.
 */


package week1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

interface Stack{
    boolean isEmpty();
    boolean isFull();
    void push(char item);
    char pop();
    char peek();
    void clear();
}

public class Solution implements Stack {
	static BufferedReader br;
	private int top;
    private int stackSize;
    private char stackArr[]; 
    
    public Solution(int stackSize) {
    	top = -1;
        this.stackSize = stackSize;
        stackArr = new char[this.stackSize];
    }    
   
    public boolean isEmpty() {
        return (top == -1);
    }
    
    public boolean isFull() {
        return (top == this.stackSize-1);
    }
    
    public void push(char item) {
        if(isFull()) {
//            System.out.println("Stack is full!");
        } else {             
            stackArr[++top] = item;
//            System.out.println("Inserted Item : " + item);
        }
    }
    
    public char peek() {
        if(isEmpty()) {
//            System.out.println("Peeking fail! Stack is empty!");
            return 0;
        } else { 
//            System.out.println("Peeked Item : " + stackArr[top]);
            return stackArr[top];
        }
    }
    
    public char pop() {
        if(isEmpty()) {
//            System.out.println("Deleting fail! Stack is empty!");
            return 0;
        } else { 
            System.out.println("Deleted Item : " + stackArr[top]);
            --top;
            return peek();//stackArr[--top]
        }                
    }
    
    public void clear() {
        if(isEmpty()) {
//            System.out.println("Stack is already empty!");
        } else {
            top = -1;
            stackArr = new char[this.stackSize];
//            System.out.println("Stack is clear!");
        }
    }
    
    public void printStack() {
        if(isEmpty()) {
            System.out.println("Stack is empty!");
        } else {
            System.out.print("Stack elements : ");
            for(int i=0; i<=top; i++) {
                System.out.print(stackArr[i] + " ");
            }
            System.out.println("top="+top);
            System.out.println();
        }
    }
    
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		int[] IO = new int[T];
		for(int i = 0; i < T; i++) {
			String S = br.readLine();
			//IO[i] = 0;
			if(S != null && S.length()%2==0)
				IO[i] = TestCase(S);
		}
		
		for(int i = 0; i < T; i++) {
			System.out.printf("Case #%d: %d\n", i+1, IO[i]);
		}

	}
	
	public static int TestCase(String S) {
		int stackSize = S.length();
		Solution arrStack = new Solution(stackSize);
		
		int result = 0;
		int cal = 0;
		
		for(int i = stackSize-1; i >= 0; i--) {
			char ch = S.charAt(i);
			System.out.println("\ni = "+i+", ch = "+ch);
			
			switch(ch) {
			case 'O': case 'o':
				arrStack.push(S.charAt(i));
				cal++;
				System.out.println("cal : "+cal);
				arrStack.printStack();
				break;
				
			case 'I':
				cal--;
				
				while(!arrStack.isEmpty() && arrStack.peek()!='O') {
					arrStack.pop();
					result++;
				}
				
			
				System.out.println("cal : "+cal);
				break;
				
			case 'i':
				cal--;
				arrStack.pop();
				arrStack.printStack();
				System.out.println("cal : "+cal);
				break;
			}
			
		}
//		arrQueue.clear();
		arrStack.clear();
		
		if(cal == 0)
			return result;
		else
			return -1;
		
	}
	

}
