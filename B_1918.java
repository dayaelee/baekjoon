import java.io.*;
import java.util.*;
public class Main {

    static int priority(char op) {
        if (op == '+' || op == '-') return 1;
        if (op == '*' || op == '/') return 2;
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringBuilder sb = new StringBuilder();
        ArrayDeque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i<str.length(); i++){
            char c = str.charAt(i);

            if (c >= 'A' && c <= 'Z'){
                sb.append(c);
            } else if (c =='('){
                stack.push(c);
            } else if (c == ')'){
                while (!stack.isEmpty() && stack.peek() != '('){
                    sb.append(stack.pop());
                }
                stack.pop();
            } else {
                while (!stack.isEmpty() && priority(stack.peek())>=priority(c)){
                    sb.append(stack.pop());
                }
                stack.push(c);
            }
        }

        while (!stack.isEmpty()){
            sb.append(stack.pop());
        }

        System.out.println(sb);
    }   
}
