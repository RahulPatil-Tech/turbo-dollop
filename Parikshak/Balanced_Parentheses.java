package Parikshak;
import java.util.Stack;
import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

/*Input: "({[()]})"
Output: Balanced
 

Input: "([)]"
Output: Not Balanced */
public class Balanced_Parentheses {
    // Simple approach to check if the parentheses are balanced
    public static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> parenthesesMap = new HashMap<>();
        parenthesesMap.put('(', ')');
        parenthesesMap.put('{', '}');
        parenthesesMap.put('[', ']');
        for (char c : s.toCharArray()) {
            if (parenthesesMap.containsKey(c)) {
                stack.push(c);
            } else if (parenthesesMap.containsValue(c)) {
                if (stack.isEmpty() || parenthesesMap.get(stack.pop()) != c) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
        }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string of parentheses: ");
        String input = scanner.nextLine();
        if (isBalanced(input)) {
            System.out.println("Balanced");
        } else {
            System.out.println("Not Balanced");
        }
        scanner.close();
    }
}