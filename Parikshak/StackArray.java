package Parikshak;
/* Implement a stack using array in c++/java, to support "push" and "pop" operation of a given size. Your program should support following commands as given below:

push N              // insert N in the stack, if stack is full print the output as "Stack Overflow" 
pop                      // Remove the last elements from the Stack and print the value and if the stack is empty print "Stack Underflow" 
exit                     // exit the program 
 assume the input will be always a positive integer.
 Sample Input/Output 1

Sample Input/Output 2

Input

3

push 8

push 7

push 6

pop 

pop

exit


Output

6

7

Input

2

pop

push 10

push 0

pop

pop

pop

exit

Output

Stack Underflow

0

10

Stack Underflow */
public class StackArray {
    private int[] stack;
    private int top;
    private int size;
    public StackArray(int size) {
        this.size = size;
        stack = new int[size];
        top = -1;
    }
    public void push(int value) {
        if (top == size - 1) {
            System.out.println("Stack Overflow");
        } else {
            stack[++top] = value;
        }
    }
    public int pop() {
        if (top == -1) {
            System.out.println("Stack Underflow");
            return -1; // Return a sentinel value to indicate underflow
        } else {
            return stack[top--];
        }
    }
    public static void main(String[] args) {
        StackArray stack = new StackArray(3);
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (true) {
            String command = scanner.nextLine();
            if (command.equals("exit")) {
                break;
            } else if (command.startsWith("push")) {
                int value = Integer.parseInt(command.split(" ")[1]);
                stack.push(value);
            } else if (command.equals("pop")) {
                int poppedValue = stack.pop();
                if (poppedValue != -1) {
                    System.out.println(poppedValue);
                }
            }
        }
        scanner.close();
    }
}
